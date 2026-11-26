---
id: subtitles-translation-mcp-focus
title: "Subtitles and Translation: Whisper plus FFmpeg"
domain: media
category: subtitles-translation
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
    install: "Skill or pip: openai-whisper"
    version_notes: "transcript-Basis for SRT"
  - name: ffmpeg
    install: "OS-Paket ffmpeg"
    version_notes: "Mux softsubs; extract audio"
  - name: Hermes-Skill youtube-content
    install: "Bundled; only for YouTube-Quelltexte"
    version_notes: "no Ersatz for lokale MP4-ASR"
inputs:
  - "Video or vorhandenes SRT"
  - "Target languages and delivery format"
  - "Translation by agent vs. CAT export"
outputs:
  - "SRT/VTT je Sprache"
  - "Optional: eingebettete softsubs"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Subtitles pipeline** plan: transcript create or import, **viasetz** with documentedm Review, **ffmpeg** for Muxen—Whisper-Skill and YouTube-content only matching the source.

## When to use

- Eigene MP4/WAV should mehrsprachig untertitelt will.
- Softsubs for Player; Hard-Burn only after approval.
- YouTube source has deactivated transcript → local ASR.

**When not to use**

- Laufschrift in Live-Sendeplan without delay-kompensierte Pipeline.
- Pure machine translation without review for legally binding content.
- Netflix/OTT-Hausformats without Spezifikation.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Whisper (Skill/CLI) | Quell-SRT | Lokal, kontrollierbar |
| ffmpeg | subs mux, extract | Standard for mov_text/srt |
| youtube-content | externes transcript | only when URL and Skill passen |
| LLM (Agent) | MT draft | Always mark as draft |

## System prompt

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

## Workflow

1. Source: file vs. YouTube vs. existing SRT.
2. at MP4: Audio extract; Whisper → `source_de.srt`.
3. SRT-Validator: Ueberlappungen, Zeilenlaenge, Mindestdauer.
4. EN translation: time-coded copy `source_en.srt` as draft.
5. Glossar-Abgleich (Marken, Produktnamen).
6. Softmux with ffmpeg for Review-Player.
7. List of open QA items for translator/human.

## Definition of done

- [ ] Timecodes unchanged across all languages (for pure translation)
- [ ] no negativen or null Dauern
- [ ] CPS and line length within agreed limits (spot check)
- [ ] MT marked as draft
- [ ] Hard-Burn only with schriftlicher approval

## Security

- Do not send confidential video content to public MT APIs without a contract.
- YouTube-transcripte: Nutzungsrechte am Video observe.

## Pitfalls

- Translating entire blocks implicitly shifts timing—work cue by cue.
- mov_text not viaall; Web oft VTT separat.
- Whisper set to wrong language → garbage—set `language` or verify auto.
- youtube-content provides placeholder examples in docs—test with a real video.
- Burn-in with wrong resolution—verify subtitles for safe margins beforehand.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** DE SRT → EN draft, same cues.
- **Input:** `training_de.srt` (84 cues).
- **Prompt:**

```text
Translate cues to English, keep timecodes, mark draft, export training_en.srt.
```

- **Expected result:**

```text
1
00:00:01,200 --> 00:00:04,800
Welcome to onboarding module three.

Cue count: 84 (unchanged timecodes)
```

### Example 2 (Example data (self-written))
- **Task:** Softsubs in MP4 muxen.
- **Input:** `course.mp4`, `course_de.srt`, approval Softsub.
- **Prompt:**

```text
Mux softsubs mov_text without re-encoding video; ffprobe streams afterward.
```

- **Expected result:**

```text
Stream #0:2(ger): Subtitle: mov_text (ger)
Video codec unchanged: h264
Output: course_de_soft.mp4
```