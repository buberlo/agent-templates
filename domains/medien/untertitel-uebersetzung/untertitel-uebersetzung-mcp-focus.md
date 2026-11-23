---
id: untertitel-uebersetzung-mcp-focus
domain: medien
title: "Untertitel und Übersetzung: Whisper plus FFmpeg"
category: untertitel-uebersetzung
tags:
  - subtitles
  - whisper
  - ffmpeg
  - translation
target_agents:
  - hermes
  - openclaw
  - generic
required_tools:
  - name: Whisper
    install: "Skill oder pip: openai-whisper"
    version_notes: "Transkript-Basis für SRT"
  - name: ffmpeg
    install: "OS-Paket ffmpeg"
    version_notes: "Mux softsubs; extract audio"
  - name: Hermes-Skill youtube-content
    install: "Bundled; nur für YouTube-Quelltexte"
    version_notes: "Kein Ersatz für lokale MP4-ASR"
inputs:
  - "Video oder vorhandenes SRT"
  - "Zielsprachen und Lieferformat"
  - "Übersetzung durch Agent vs. CAT-Export"
outputs:
  - "SRT/VTT je Sprache"
  - "Optional: eingebettete softsubs"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Untertitel-Pipeline** planen: Transkript erzeugen oder importieren, **übersetzen** mit dokumentiertem Review, **ffmpeg** zum Muxen—Whisper-Skill und youtube-content nur passend zur Quelle.

## Wann nutzen

- Eigene MP4/WAV soll mehrsprachig untertitelt werden.
- Softsubs für Player; Hard-Burn nur nach Freigabe.
- YouTube-Quelle hat deaktiviertes Transkript → lokale ASR.

**Wann nicht**

- Laufschrift in Live-Sendeplan ohne delay-kompensierte Pipeline.
- Reine maschinelle Übersetzung ohne Review für rechtlich bindende Inhalte.
- Netflix/OTT-Hausformats ohne Spezifikation.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Whisper (Skill/CLI) | Quell-SRT | Lokal, kontrollierbar |
| ffmpeg | subs mux, extract | Standard für mov_text/srt |
| youtube-content | externes Transkript | Nur wenn URL und Skill passen |
| LLM (Agent) | MT-Entwurf | Immer als draft markieren |

## System-Prompt / Instruktionen

```text
You deliver subtitle files and optional muxed videos for localization.

Inputs: source media or SRT, source language, target languages[], delivery (srt, vtt, embedded softsubs), burn-in (forbidden unless approved), reading speed limits (CPS ~17 for DE entertainment default).

Pipeline A (no SRT): ffmpeg extract 16k wav → whisper → source.srt → QA timings.

Pipeline B (has SRT): validate format, fix overlapping cues, then translate cue-by-cue preserving timecodes.

Translation:
- Never shift timestamps when translating text only.
- Mark draft MT; list idioms and numbers that need human check.
- For proper nouns use user glossary if provided.

Mux: ffmpeg -i video.mp4 -i subs_de.srt -c copy -c:s mov_text out_de.mp4
VTT: convert from SRT with consistent WEBVTT header.

youtube-content: only when user supplies YouTube URL and needs text—not for mux to arbitrary mkv.

Approvals: burn-in, public upload, and distribution require explicit user yes.

Output: per-language files, glossary additions, mux commands, unresolved QA flags.

Export a cue index CSV for CAT tools when user mentions memoQ or Phrase.
If burn-in requested, render test 30s segment before full file.
Honor platform safe margins (e.g. 10% bottom) in review notes even for softsubs.
```

## Arbeitsablauf

1. Quelle klären: Datei vs. YouTube vs. vorhandenes SRT.
2. Bei MP4: Audio extrahieren; Whisper → `source_de.srt`.
3. SRT-Validator: Überlappungen, Zeilenlänge, Mindestdauer.
4. Übersetzung EN: zeitkodierte Kopie `source_en.srt` als Entwurf.
5. Glossar-Abgleich (Marken, Produktnamen).
6. Softmux mit ffmpeg für Review-Player.
7. Liste offener QA-Punkte an Übersetzer/Mensch.

## Qualitätskriterien / Definition of Done

- [ ] Timecodes unverändert über alle Sprachen (bei reiner Übersetzung)
- [ ] Keine negativen oder null Dauern
- [ ] CPS und Zeilenlänge im vereinbarten Rahmen (Stichprobe)
- [ ] MT als Entwurf gekennzeichnet
- [ ] Hard-Burn nur mit schriftlicher Freigabe

## Sicherheit & Freigaben

- Vertrauliche Video-Inhalte nicht an öffentliche MT-APIs ohne Vertrag.
- YouTube-Transkripte: Nutzungsrechte am Video beachten.

## Fallstricke

- Übersetzung ganzer Blöcke verschiebt implizit Timing—cueweise arbeiten.
- mov_text nicht überall; Web oft VTT separat.
- Whisper auf falscher Sprache → Garbage—`language` setzen oder auto prüfen.
- youtube-content liefert Platzhalter-Beispiele in Doku—echtes Video testen.
- Burn-in mit falscher Auflösung—subs vorher auf safe margin prüfen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** DE SRT → EN Entwurf, gleiche Cues.
- **Input:** `training_de.srt` (84 cues).
- **Prompt:**

```text
Translate cues to English, keep timecodes, mark draft, export training_en.srt.
```

- **Erwartetes Ergebnis:**

```text
1
00:00:01,200 --> 00:00:04,800
Welcome to onboarding module three.

Cue count: 84 (unchanged timecodes)
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Softsubs in MP4 muxen.
- **Input:** `course.mp4`, `course_de.srt`, Freigabe Softsub.
- **Prompt:**

```text
Mux softsubs mov_text without re-encoding video; ffprobe streams afterward.
```

- **Erwartetes Ergebnis:**

```text
Stream #0:2(und): Subtitle: mov_text (ger)
Video codec unchanged: h264
Output: course_de_soft.mp4
```