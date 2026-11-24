---
id: audio-whisper-transcribe-diarize
title: "Transcription and Sprechersegmente with Whisper"
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
    install: "pip: pyannote.audio (HF-Token for Diarisierung)"
    version_notes: "only at expliziter approval and Token"
  - name: ffmpeg
    install: "OS-Paket ffmpeg"
    version_notes: "Audio extract, 16 kHz mono for ASR"
inputs:
  - "Audio- or Videodatei"
  - "Sprache(n) and gewuenschtes Format (SRT, VTT, JSON)"
  - "Optional: Sprecheranzahl or Diarisierung ja/nein"
outputs:
  - "transcript with Timestamps"
  - "Optional: SRT with Sprecher-Praefixen"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Zeitlich verknuepfte transcripte** and optional **Sprechersegmente** for Subtitles, Uebersetzung and Barrierefreiheit—lokal with Whisper, Diarisierung only at freigegebenem Setup.

## When to use

- Internes Training, Podcast or Webinar should untertitelt will.
- Rohmaterial liegt as MP4/MKV/WAV before; Genauigkeit wichtiger as Echtzeit.
- OpenClaw Whisper-Skill or CLI is verfuegbar.

**When not to use**

- Broadcast-Subtitles with strengen CEA-608/EBU-Timing-Vorgaben without QA-Mensch.
- Inhalt unter Strafverfolgung/Anwaltsgeheimnis without juristische approval for ML-Verarbeitung.
- Reine Uebersetzung from bereits perfektem SRT (dann CAT-Workflow statt Re-ASR).

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
5. at Diarisierung: pyannote → `segments.json`; with Whisper-Segmenten merge.
6. `ffmpeg -i input.mp4 -i work/audio.srt -c copy -c:s srt -metadata:s:s:0 language=de out_soft.mkv` only after approval.
7. Stichprobe: 3 zufaellige Intervalle im Player against Text abgleichen.

## Definition of done

- [ ] Timestamps monoton steigend; no Ueberlappung in SRT
- [ ] Sprache korrekt erkannt or explizit gesetzt
- [ ] Eigennamen/Fachbegriffe markiert, when unsicher
- [ ] Diarisierung only when angefordert and dokumentiert
- [ ] Quellaudio not in fremde Cloud hochgeladen

## Security

- voicesbiometrie and personenbezogene Inhalte: approval and Loeschfrist for `work/`.
- HF-Token and API-Keys not committen.
- Oeffentliche YouTube-Subtitles: copyright am Quellvideo clarify.

## Pitfalls

- Musik unter Sprache → Phantom-Text; VAD or manuelles Skip.
- Diarisierung + Whisper-Offsets falsch gemergt → wechselnde falsche Labels.
- 25 fps vs 30 fps Video: SRT from Audio oft passt, aber eingebettete VTT braucht gleiche timebase.
- Grosse Modelle on CPU: Stunden Laufzeit—Batch nachts plan.
- Automatische Uebersetzung without Review verletzt Markentonalitaet.

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
- **Task:** Zwei Sprecher, Diarisierung from.
- **Input:** Interview WAV, only transcript JSON for Uebersetzer.
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