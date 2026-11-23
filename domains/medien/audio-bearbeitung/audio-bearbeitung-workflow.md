---
id: audio-bearbeitung-workflow
domain: medien
title: "Audio schneiden, normalisieren und konvertieren"
category: audio-bearbeitung
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
    version_notes: "Nur für Transkript nach Audio-Prep"
inputs:
  - "Quellaudio (beliebiges Format)"
  - "Ziel (Format, Lautheit, Schnitt)"
outputs:
  - "Bearbeitete Audiodatei"
  - "Optional Transkript"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Allgemeine **Audio-Postproduktion** mit FFmpeg: extrahieren, schneiden, loudnorm, Formatwechsel—optional Anschluss an Whisper für Transkript, ohne DAW-Pflicht.

## Wann nutzen

- Sprachmemos, Sessions oder Extrakte aus Video sollen hörbar und einheitlich werden.
- Batch-Konvertierung WAV→FLAC/MP3 mit gleichen Parametern.
- Agent soll Befehlskette dokumentieren.

**Wann nicht**

- MIDI/virtuelle Instrumente mixen.
- Autotune und Melodie-Korrektur auf Takes.
- Surround-5.1-Mastering für Kino.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ffmpeg | Schnitt, Filter, Encode | Ein Werkzeug für die meisten Jobs |
| ffprobe | Analyse | Codec, layout, duration |
| Whisper Skill | Transkript | Optional zweiter Schritt |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. `ffprobe input` — Kanäle, Rate, Dauer.
2. Aus Video: `ffmpeg -i clip.mp4 -vn -map 0:a:0 -c:a pcm_s16le audio.wav`.
3. Schnitt: `ffmpeg -i audio.wav -ss 5 -to 120 -c copy trimmed.wav` oder re-encode bei MP3.
4. loudnorm two-pass auf `trimmed.wav`.
5. Export MP3/FLAC je Briefing.
6. Optional Whisper auf WAV.
7. Summary: Peak, LUFS, Pfad.

## Qualitätskriterien / Definition of Done

- [ ] Ausgabeformat und -rate wie spezifiziert
- [ ] Kein Clipping (true peak ≤ -1 dBTP wenn normalisiert)
- [ ] Schnitt an richtigen Zeitmarken ±0,1 s
- [ ] Befehlsprotokoll vollständig

## Sicherheit & Freigaben

- Vertrauliche Gespräche lokal halten; Cloud-Transkription nur mit Freigabe.

## Fallstricke

- MP3-Schnitt mit `-c copy` an Frame-Grenzen unsauber.
- Stereo zu Mono ohne `-ac 1` kann Phasen-Mono-Effekt ignorieren—`-pan` nur bewusst.
- loudnorm auf Musik-Mix verfälscht Dynamik.
- Mehrfaches Transcodieren MP3→AAC→MP3: Generationsverlust.
- Whisper auf 8 kHz Telefon-Audio ohne Upsample.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Audio aus Zoom-MP4, -24 LUFS grob normalisieren.
- **Input:** `meeting.mp4`, 62 min.
- **Prompt:**

```text
Extract audio to 48k wav, two-pass loudnorm -24 LUFS for archive, log commands.
```

- **Erwartetes Ergebnis:**

```bash
ffmpeg -i meeting.mp4 -vn -ar 48000 meeting.wav
# loudnorm two-pass → meeting_norm.wav, integrated ≈ -24 LUFS
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** 3 Voice-Memos zu einem FLAC.
- **Input:** `memo1.m4a`, `memo2.m4a`, `memo3.m4a`.
- **Prompt:**

```text
Concat to single FLAC 48k stereo; resample each input first.
```

- **Erwartetes Ergebnis:**

```
concat_list.txt → combined.flac
ffprobe: 1 stream, flac, 48000 Hz, stereo, duration sum ±0.1s
```