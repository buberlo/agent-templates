---
id: video-ffmpeg-cut-transcode
domain: medien
title: "Video schneiden, transcodieren und Untertitel"
category: video-bearbeitung
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
    install: "OS-Paket: ffmpeg (ffprobe mitgeliefert)"
    version_notes: "FFmpeg 6.x/7.x; libx264 und AAC verfügbar"
  - name: ffprobe
    install: "Teil des ffmpeg-Pakets"
    version_notes: "JSON-Ausgabe für Automatisierung"
  - name: whisper
    install: "pip: openai-whisper oder whisper.cpp CLI"
    version_notes: "large-v3-turbo für DE/EN; GPU optional"
inputs:
  - "Quellvideo (MP4, MOV, MKV)"
  - "Schnittfenster (IN/OUT oder -ss/-to)"
  - "Zielprofil (Auflösung, Codec, Container)"
  - "Optional: Untertitel (ASR oder lieferbare SRT)"
outputs:
  - "Fertiges MP4 mit web-tauglichem Profil"
  - "Optional: SRT/VTT und Befehlsprotokoll"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Dieses Template steuert Agenten bei **Schnitt**, **Transcodierung** und optionaler **Untertitel-Erzeugung** aus Rohtakes—ohne NLE, mit reproduzierbaren FFmpeg-Befehlen und nachvollziehbarer Qualitätskontrolle.

## Wann nutzen

- Kunde liefert eine oder wenige Dateien; Auslieferung soll einheitliches H.264/AAC-MP4 plus optionale Untertitel sein.
- Schnitt ist linear (ein IN/OUT-Block oder wenige Segmente); kein Multicam-Sync.
- Agent hat Shell-Zugriff auf `ffmpeg`/`ffprobe` (kein dediziertes Video-MCP nötig).

**Wann nicht**

- Color Grading, komplexes Compositing oder Frame-genaue Fusion mehrerer Kameras.
- DRM-geschützte Quellen oder Broadcast-Mezzanine mit strikten Hausnormen ohne Freigabeprofil.
- Einarbeitung in Social-Reels mit Plattform-API-Upload (dafür eigene Publishing-Templates).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ffprobe | Metadaten, Dauer, Codecs | Entscheidung copy vs. re-encode vor dem Schnitt |
| ffmpeg | Schnitt, Skalierung, Encode, mux | De-facto-Standard, scriptbar |
| Whisper | ASR → SRT | Offline-fähig für DE/EN; nur bei Freigabe |
| sed/awk | SRT-Zeitkorrektur | Kleine Offsets ohne Re-Encode |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. `ffprobe -v quiet -print_format json -show_format -show_streams input.mov` auswerten; Schnittfenster gegen Dauer prüfen.
2. Rohschnitt: `ffmpeg -i input.mov -ss 00:01:12.000 -to 00:04:05.000 -c copy cut.mkv` nur wenn Codec/Container passen; sonst Re-Encode-Zweig.
3. Transcode: `ffmpeg -i cut.mkv -vf scale=-2:1080 -c:v libx264 -crf 20 -preset medium -c:a aac -b:a 192k -movflags +faststart deliver.mp4`.
4. Optional Whisper: `whisper deliver.mp4 --language de --output_format srt --output_dir ./subs/`.
5. VTT aus SRT ableiten oder `ffmpeg -i deliver.mp4 -i subs.srt -c copy -c:s mov_text deliver_subs.mp4` nach Freigabe für Softsubs.
6. QA: `ffprobe deliver.mp4`, Stichprobe mit `ffplay` oder Framegrab `ffmpeg -ss 30 -i deliver.mp4 -frames:v 1 qa.jpg`.

## Qualitätskriterien / Definition of Done

- [ ] Ausgabedauer weicht höchstens ±0,5 s vom Schnittfenster ab
- [ ] Video `yuv420p`, Audio ohne Clipping; `-movflags +faststart` gesetzt
- [ ] Kein sichtbarer A/V-Drift in Stichproben
- [ ] Untertitel zeitlich plausibel (falls erzeugt); Eigennamen stichprobenartig geprüft
- [ ] Alle FFmpeg-Befehle im Thread oder Log dokumentiert

## Sicherheit & Freigaben

- Keine Uploads auf Cloud-Transcoder oder Video-Hosting ohne Kundenfreigabe.
- Meeting-Audio, Gesichter und Stimmen nur mit DSGVO-/Vertraulichkeitsfreigabe transkribieren.
- Hard-Burn-Untertitel und irreversible Deletes nur nach expliziter Bestätigung.

## Fallstricke

- `-c copy` bei Schnitten auf nicht-Keyframe-nahen `-ss`-Werten erzeugt schwarze Frames oder Audio-Vorspann—bei Unsicherheit re-encoden.
- `-ss` vor `-i` ist schneller, aber ungenauer; für Auslieferungen mit Frame-Toleranz `<1s` `-ss` nach `-i` nutzen.
- Vertikale iPhone-Movies: Rotation-Metadaten vs. tatsächliche Pixel—`ffprobe` und Testframe prüfen.
- `loudnorm` zweimal anwenden oder auf bereits limitiertes Material—Pumping und Verzerrung.
- Whisper halluziniert bei Musik und Überlagerung—SRT manuell gegen Audio stichproben.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Firmen-Interview aus 4K-MOV auf 1080p-Web-MP4 kürzen.
- **Input:** `interview.mov` (3840×2160, 12:40), Schnitt `00:00:45`–`00:08:20`, Ziel 1080p H.264.
- **Prompt:**

```text
Probe interview.mov, cut 45s–8m20s, transcode to 1080p H.264 AAC with faststart. No subtitles. Document commands.
```

- **Erwartetes Ergebnis:**

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 interview.mov
# → 760.0
ffmpeg -i interview.mov -ss 00:00:45 -to 00:08:20 -vf scale=-2:1080 -c:v libx264 -crf 21 -c:a aac -b:a 160k -movflags +faststart interview_1080p.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 interview_1080p.mp4
# → 455.2
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Soft-Untertitel für internes Training (nur Intranet).
- **Input:** `training.mp4` (720p), Freigabe für Whisper DE.
- **Prompt:**

```text
Transcribe training.mp4 to German SRT with Whisper, fix obvious proper nouns, mux as soft subtitle track mov_text. No burn-in.
```

- **Erwartetes Ergebnis:**

```text
1
00:00:01,200 --> 00:00:04,800
Willkommen zum Onboarding-Modul drei.

Output: training_de.srt, training_subs.mp4 (video copy + mov_text), ffprobe lists Stream #0:2 subtitle.
```