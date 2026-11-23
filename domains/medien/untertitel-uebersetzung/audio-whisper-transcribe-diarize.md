---
id: audio-whisper-transcribe-diarize
domain: medien
title: "Transkription und Sprechersegmente mit Whisper"
category: untertitel-uebersetzung
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
    install: "pip: pyannote.audio (HF-Token für Diarisierung)"
    version_notes: "Nur bei expliziter Freigabe und Token"
  - name: ffmpeg
    install: "OS-Paket ffmpeg"
    version_notes: "Audio extrahieren, 16 kHz mono für ASR"
inputs:
  - "Audio- oder Videodatei"
  - "Sprache(n) und gewünschtes Format (SRT, VTT, JSON)"
  - "Optional: Sprecheranzahl oder Diarisierung ja/nein"
outputs:
  - "Transkript mit Timestamps"
  - "Optional: SRT mit Sprecher-Präfixen"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Zeitlich verknüpfte Transkripte** und optional **Sprechersegmente** für Untertitel, Übersetzung und Barrierefreiheit—lokal mit Whisper, Diarisierung nur bei freigegebenem Setup.

## Wann nutzen

- Internes Training, Podcast oder Webinar soll untertitelt werden.
- Rohmaterial liegt als MP4/MKV/WAV vor; Genauigkeit wichtiger als Echtzeit.
- OpenClaw Whisper-Skill oder CLI ist verfügbar.

**Wann nicht**

- Broadcast-Untertitel mit strengen CEA-608/EBU-Timing-Vorgaben ohne QA-Mensch.
- Inhalt unter Strafverfolgung/Anwaltsgeheimnis ohne juristische Freigabe für ML-Verarbeitung.
- Reine Übersetzung aus bereits perfektem SRT (dann CAT-Workflow statt Re-ASR).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ffmpeg | 16 kHz mono WAV | Whisper-Eingangsformat |
| Whisper | Wort-/Segment-Timestamps | Offline, mehrsprachig |
| pyannote | Sprecherlabels | Optional; HF-Token nötig |
| sed/python | SRT formatieren | Zeilenlängen, CPS-Limits |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. `ffprobe input.mp4` — Audiospur und Dauer notieren.
2. `ffmpeg -i input.mp4 -vn -ac 1 -ar 16000 audio.wav`.
3. `whisper audio.wav --model large-v3-turbo --language de --output_dir work/`.
4. `audio.srt` auf Zeilenlänge prüfen; Skript `split_long_lines.py` optional.
5. Bei Diarisierung: pyannote → `segments.json`; mit Whisper-Segmenten mergen.
6. `ffmpeg -i input.mp4 -i work/audio.srt -c copy -c:s srt -metadata:s:s:0 language=de out_soft.mkv` nur nach Freigabe.
7. Stichprobe: 3 zufällige Intervalle im Player gegen Text abgleichen.

## Qualitätskriterien / Definition of Done

- [ ] Timestamps monoton steigend; keine Überlappung in SRT
- [ ] Sprache korrekt erkannt oder explizit gesetzt
- [ ] Eigennamen/Fachbegriffe markiert, wenn unsicher
- [ ] Diarisierung nur wenn angefordert und dokumentiert
- [ ] Quellaudio nicht in fremde Cloud hochgeladen

## Sicherheit & Freigaben

- Stimmenbiometrie und personenbezogene Inhalte: Freigabe und Löschfrist für `work/`.
- HF-Token und API-Keys nicht committen.
- Öffentliche YouTube-Untertitel: Urheberrecht am Quellvideo klären.

## Fallstricke

- Musik unter Sprache → Phantom-Text; VAD oder manuelles Skip.
- Diarisierung + Whisper-Offsets falsch gemergt → wechselnde falsche Labels.
- 25 fps vs 30 fps Video: SRT aus Audio oft passt, aber eingebettete VTT braucht gleiche timebase.
- Große Modelle auf CPU: Stunden Laufzeit—Batch nachts planen.
- Automatische Übersetzung ohne Review verletzt Markentonalität.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** DE-Untertitel für 8-min-Explainer.
- **Input:** `explainer.mp4`, Sprache Deutsch.
- **Prompt:**

```text
Extract audio, whisper large-v3-turbo DE, produce explainer.srt max 42 chars/line, flag low confidence.
```

- **Erwartetes Ergebnis:**

```text
1
00:00:00,000 --> 00:00:03,400
Heute zeigen wir das neue Dashboard.

Low confidence: none above threshold
Duration coverage: 00:07:58.2 / 00:08:00.0
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Zwei Sprecher, Diarisierung aus.
- **Input:** Interview WAV, nur Transkript JSON für Übersetzer.
- **Prompt:**

```text
Whisper JSON only, no diarization, include segment-level timestamps for CAT import.
```

- **Erwartetes Ergebnis:**

```json
{
  "segments": [
    { "start": 0.0, "end": 4.2, "text": "Guten Tag, willkommen." },
    { "start": 4.5, "end": 9.1, "text": "Danke, schön hier zu sein." }
  ]
}
```