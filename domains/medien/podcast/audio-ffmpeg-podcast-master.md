---
id: audio-ffmpeg-podcast-master
domain: medien
title: "Podcast-Mastering mit FFmpeg"
category: podcast
tags:
  - podcast
  - ffmpeg
  - loudnorm
  - mastering
target_agents:
  - hermes
  - openclaw
  - generic
required_tools:
  - name: ffmpeg
    install: "OS-Paket ffmpeg (libavfilter loudnorm)"
    version_notes: "EBU R128 loudnorm Filter; afftdn optional"
  - name: ffprobe
    install: "Teil von ffmpeg"
    version_notes: "Peaks und Dauer vor Mastering"
inputs:
  - "Roh-Audio (WAV/MP3 aus Recorder oder Riverside)"
  - "Ziel-Lautheit (z. B. -16 LUFS integriert für Podcast)"
  - "Optional: Intro/Outro-Clips"
outputs:
  - "Master-MP3 oder AAC für Hosting"
  - "Loudness-Report (eingebettet oder Log)"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Einheitliche **Lautheit**, **sicherer Headroom** und **exportfertige Podcast-Folgen** per FFmpeg—Intro/Outro-Mix, leichte Rauschreduktion und dokumentierte Zielwerte für Spotify/Apple.

## Wann nutzen

- Doppelspur oder Einzelspur-WAV liegt vor; keine DAW-Session nötig.
- Wiederkehrendes Mastering-Profil (-16 LUFS, mono/stereo klar definiert).
- Shownotes/Transkript folgen in separatem Schritt (Whisper-Skill).

**Wann nicht**

- Musik-lastige Produktion mit Stem-Mix und komplexem Bus-Routing.
- De-Esser und manuelles Dialogue-Edit auf Wortebene (DAW + Mensch).
- Live-Recording mit Round-Trip-Latenz-Korrektur.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ffmpeg loudnorm | EBU R128 Ziel | Podcast-Plattform-Erwartungen |
| ffmpeg afftdn / highpass | Rauschunterdrückung | Vorsichtig, nur bei Bedarf |
| ffmpeg concat | Intro/Outro | Dateiliste ohne Re-Export der Mitte |
| ffprobe | Peaks, codec | Vorher/nachher dokumentieren |

## System-Prompt / Instruktionen

```text
You master podcast audio with ffmpeg filters for loudness and light cleanup.

Inputs: source path, target integrated loudness (default -16 LUFS for stereo podcast), true peak ceiling (default -1.0 dBTP), mono force (yes/no), intro/outro paths optional.

Always ffprobe input: sample rate, channels, duration, max volume estimate via volumedetect on a 60s sample if file is long.

First pass (analysis): ffmpeg -i voice.wav -af loudnorm=I=-16:TP=-1.0:LRA=11:print_format=json -f null - 2> loudnorm_first.json
Parse measured_I, measured_TP, measured_LRA, measured_thresh, offset.

Second pass (apply): use loudnorm with measured_* values for linear normalization; add aresample=async=1 if sample rates differ in concat.

Concat: use concat demuxer with matching sample rate (44100 or 48000) and channel layout; resample extras first.

Noise: only apply afftdn=nr=12 if user reports room tone; never on music beds without approval.

Export: libmp3lame -q:a 2 for MP3 or aac -b:a 192k for M4A; include ID3 title/artist only if user supplies metadata.

Verify: run loudnorm print_format=summary on output; integrated within ±0.5 LUFS of target.

List every filter chain. No publishing to RSS or Spotify without explicit approval.

If guest and host are separate files, sync via loudnorm per track before concat.
Note integrated loudness before and after in a small table for host sign-off.
When intro music under speech, ducking is out of scope unless user supplies sidechain spec.
Archive raw guest file checksum (sha256) in log for dispute resolution.
```

## Arbeitsablauf

1. `ffprobe -show_streams episode_raw.wav` — 48 kHz stereo bestätigen.
2. Stille am Anfang/Ende: optional `silenceremove` nur mit Freigabe (kann Atmosphäre kappen).
3. `ffmpeg -i episode_raw.wav -af loudnorm=...:print_format=json -f null -` → Messwerte speichern.
4. Zweiter Durchlauf mit `measured_*` aus JSON; Ausgabe `episode_norm.wav`.
5. Intro/Outro: `ffmpeg -i intro.wav -i episode_norm.wav -i outro.wav -filter_complex concat=n=3:v=0:a=1 -ar 48000 final.wav`.
6. Encode: `ffmpeg -i final.wav -codec:a libmp3lame -q:a 2 episode.mp3`.
7. `ffmpeg -i episode.mp3 -af loudnorm=print_format=summary -f null -` zur Abnahme loggen.

## Qualitätskriterien / Definition of Done

- [ ] Integrated Loudness im Zielkorridor (±0,5 LUFS)
- [ ] True Peak ≤ vereinbartem Ceiling
- [ ] Kein hörbares Pumping durch doppeltes loudnorm auf bereits limitiertem Material
- [ ] Intro/Outro ohne Klick oder Sample-Rate-Mismatch
- [ ] Filtergraph und Zielwerte im Protokoll

## Sicherheit & Freigaben

- Gaststimmen und vertrauliche Inhalte nicht an Cloud-Mastering-Dienste senden ohne Vertrag.
- Veröffentlichung bei Hosting-Plattformen nur nach expliziter Freigabe.

## Fallstricke

- Einmalige loudnorm ohne zweiten Pass mit `measured_*` ist oft ungenau—Zwei-Pass-Workflow einhalten.
- MP3-Erzeugung vor loudnorm macht Messungen unzuverlässig—zuerst WAV master, dann Lossy.
- Mono-Spur als fake stereo (`pan`) kann Phase-Probleme erzeugen—lieber explizit `-ac 1`.
- aggressive `afftdn` entfemt „S“-Laute—Nurstufen testen.
- Concat mit unterschiedlichen Sample-Rates ohne `aresample` → Pitch-Fehler.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Interview-Spur auf -16 LUFS bringen.
- **Input:** `guest.wav`, 41:02, 48 kHz mono.
- **Prompt:**

```text
Two-pass loudnorm to -16 LUFS, -1 dBTP, keep mono. Export episode_guest.mp3 q:a 2. Log final loudnorm summary.
```

- **Erwartetes Ergebnis:**

```text
Input max_volume: -4.2 dB
Output loudnorm:
  Input Integrated:  -16.1 LUFS
  Output True Peak:  -1.1 dBTP
File: episode_guest.mp3 (duration 2462s)
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Intro 12 s + Episode + Outro 8 s concatenieren.
- **Input:** `intro.wav`, `body_norm.wav`, `outro.wav` (alle 48 kHz stereo).
- **Prompt:**

```text
Concat intro, body, outro to final.wav then MP3. Verify no sample rate mismatch.
```

- **Erwartetes Ergebnis:**

```
ffconcat version 1.0
file 'intro.wav'
file 'body_norm.wav'
file 'outro.wav'
→ final.mp3, ffprobe duration = intro+body+outro ±0.05s
```