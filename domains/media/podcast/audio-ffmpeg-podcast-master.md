---
id: audio-ffmpeg-podcast-master
title: "Podcast-Mastering with FFmpeg"
domain: media
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
    install: "Teil of ffmpeg"
    version_notes: "Peaks and Dauer before Mastering"
inputs:
  - "Roh-Audio (WAV/MP3 from Recorder or Riverside)"
  - "Target loudness (z. B. -16 LUFS integriert for Podcast)"
  - "Optional: Intro/Outro-Clips"
outputs:
  - "Master-MP3 or AAC for Hosting"
  - "Loudness-Report (eingebettet or Log)"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Consistent **loudness**, **safe headroom**, and **delivery-ready podcast episodes** via FFmpeg—intro/outro mix, light noise reduction, and documented targets for Spotify/Apple.

## When to use

- Doppelspur or Einzelspur-WAV liegt before; no DAW-Session required.
- Recurring mastering profile (-16 LUFS, mono/stereo clearly defined).
- Shownotes/transcript folgen in separatem step (Whisper-Skill).

**When not to use**

- Musik-lastige Produktion with Stem-Mix and komplexem Bus-Routing.
- De-Esser and manuelles Dialogue-Edit on Wortebene (DAW + Mensch).
- Live-Recording with Round-Trip-Latenz-Korrektur.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| ffmpeg loudnorm | EBU R128 Target | Podcast-Plattform-Erwartungen |
| ffmpeg afftdn / highpass | Rauschunterdrueckung | Vorsichtig, only at Bedarf |
| ffmpeg concat | Intro/Outro | fileliste without Re-Export the Mitte |
| ffprobe | Peaks, codec | Before/after document |

## System prompt

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

## Workflow

1. `ffprobe -show_streams episode_raw.wav` — 48 kHz stereo bestaetigen.
2. Stille am Anfang/Ende: optional `silenceremove` only with approval (kann Atmosphaere kappen).
3. `ffmpeg -i episode_raw.wav -af loudnorm=...:print_format=json -f null -` → Messwerte speichern.
4. Zweiter Durchlauf with `measured_*` from JSON; Ausgabe `episode_norm.wav`.
5. Intro/Outro: `ffmpeg -i intro.wav -i episode_norm.wav -i outro.wav -filter_complex concat=n=3:v=0:a=1 -ar 48000 final.wav`.
6. Encode: `ffmpeg -i final.wav -codec:a libmp3lame -q:a 2 episode.mp3`.
7. `ffmpeg -i episode.mp3 -af loudnorm=print_format=summary -f null -` zur approval loggen.

## Definition of done

- [ ] Integrated Loudness im Targetkorridor (±0,5 LUFS)
- [ ] True Peak ≤ vereinbartem Ceiling
- [ ] no hoerbares Pumping durch doppeltes loudnorm on bereits limitiertem Material
- [ ] Intro/Outro without Klick or Sample-Rate-Mismatch
- [ ] Filtergraph and target values im Protokoll

## Security

- Gaststimmen and vertrauliche Inhalte not an Cloud-Mastering-Dienste senden without Vertrag.
- Veroeffentlichung at Hosting-Plattformen only after expliziter approval.

## Pitfalls

- Einmalige loudnorm without zweiten Pass with `measured_*` is oft ungenau—Zwei-Pass-Workflow einhalten.
- MP3-generation before loudnorm macht Messungen unzuverlaessig—first WAV master, dann Lossy.
- Mono-Spur as fake stereo (`pan`) kann Phase-Probleme create—lieber explizit `-ac 1`.
- aggressive `afftdn` entfemt „S“-Laute—Nurstufen testen.
- Concat with unterschiedlichen Sample-Rates without `aresample` → Pitch-Fehler.

## Basic examples

### Example 1 (Example data)

- **Task:** Interview-Spur on -16 LUFS bringen.
- **Input:** `guest.wav`, 41:02, 48 kHz mono.
- **Prompt:**

```text
Two-pass loudnorm to -16 LUFS, -1 dBTP, keep mono. Export episode_guest.mp3 q:a 2. Log final loudnorm summary.
```

- **Expected result:**

```text
Input max_volume: -4.2 dB
Output loudnorm:
  Input Integrated:  -16.1 LUFS
  Output True Peak:  -1.1 dBTP
File: episode_guest.mp3 (duration 2462s)
```

### Example 2 (Example data)

- **Task:** Intro 12 s + Episode + Outro 8 s concatenieren.
- **Input:** `intro.wav`, `body_norm.wav`, `outro.wav` (all 48 kHz stereo).
- **Prompt:**

```text
Concat intro, body, outro to final.wav then MP3. Verify no sample rate mismatch.
```

- **Expected result:**

```
ffconcat version 1.0
file 'intro.wav'
file 'body_norm.wav'
file 'outro.wav'
→ final.mp3, ffprobe duration = intro+body+outro ±0.05s
```