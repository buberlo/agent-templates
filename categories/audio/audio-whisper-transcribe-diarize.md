---
id: audio-whisper-transcribe-diarize
title: "Audio transkribieren und Sprecher trennen"
category: audio
tags:
  - whisper
  - transcription
  - diarization
target_agents:
  - hermes
  - generic
required_tools:
  - name: whisper
    install: "pip: openai-whisper"
    version_notes: "large-v3; GPU optional"
  - name: whisperx
    install: "pip: whisperx"
    version_notes: "Alignment + Diarization mit pyannote"
inputs:
  - "Audio/WAV/MP3"
  - "Sprache (de/en)"
  - "Optional: Sprecheranzahl"
outputs:
  - "Transcript TXT/MD"
  - "SRT mit Sprecherlabels"
risk_level: low
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Lange Aufnahmen in durchsuchbare Transkripte mit optionaler Sprecherzuordnung umwandeln.

## Wann nutzen

- Meetings, Podcast-Rohtakes, Interview-Audio vor Schnitt.
- Nicht für Musikproduktion oder stem separation (dafür Demucs).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ffmpeg | Normalisierung | Mono 16 kHz für ASR |
| Whisper | ASR | Robuste DE/EN |
| WhisperX | Diarization | Zeitliche Sprecherlabels |

## System-Prompt / Instruktionen

```text
Transcribe audio with whisper/whisperx.
1) ffmpeg normalize to 16kHz mono wav if needed.
2) Run whisper with language hint; output segments.
3) If diarization requested: whisperx with speaker count or auto.
4) Export SRT with SPEAKER_XX prefixes; redact PII on request.
Never upload audio to third parties without approval.
```

## Arbeitsablauf

1. Metadaten per `ffprobe`; Lautstärke normalisieren.
2. Whisper-Lauf; Qualität stichprobenartig prüfen.
3. Optional WhisperX für Diarization.
4. Glossar/Firmennamen manuell korrigieren.
5. Lieferung: Markdown + SRT.

## Qualitätskriterien / Definition of Done

- [ ] Wortfehlerquote unter vereinbarter Schwelle
- [ ] Timestamps monoton steigend
- [ ] Sprecherlabels konsistent (falls Diarization)

## Sicherheit & Freigaben

- Aufnahmen können PII enthalten; Speicherung nur verschlüsselt.
- pyannote/HuggingFace-Token nicht in Logs.

## Beispiele

**Eingabe:** `standup_45min.m4a`, Sprache `de`
**Erwartetes Ergebnis:** `standup.md`, `standup.srt`
