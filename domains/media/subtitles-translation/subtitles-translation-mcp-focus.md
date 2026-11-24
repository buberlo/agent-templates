---
id: subtitles-translation-mcp-focus
title: "Subtitles and Uebersetzung: Whisper plus FFmpeg"
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
  - "Targetsprachen and Lieferformat"
  - "Uebersetzung durch Agent vs. CAT-Export"
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
- Reine maschinelle Uebersetzung without Review for rechtlich bindende Inhalte.
- Netflix/OTT-Hausformats without Spezifikation.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Whisper (Skill/CLI) | Quell-SRT | Lokal, kontrollierbar |
| ffmpeg | subs mux, extract | Standard for mov_text/srt |
| youtube-content | externes transcript | only when URL and Skill passen |
| LLM (Agent) | MT-Entwurf | Immer as draft markieren |

## System prompt

```text
You deliver subtitle files and optional muxed videos for localization.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


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
Honor platform safe margins (e.g. 10% bottom) in review notes even for softsubs.```

## Workflow

1. Source: file vs. YouTube vs. existing SRT.
2. at MP4: Audio extract; Whisper → `source_de.srt`.
3. SRT-Validator: Ueberlappungen, Zeilenlaenge, Mindestdauer.
4. Uebersetzung EN: zeitkodierte Kopie `source_en.srt` as Entwurf.
5. Glossar-Abgleich (Marken, Produktnamen).
6. Softmux with ffmpeg for Review-Player.
7. list offener QA-Punkte an Uebersetzer/Mensch.

## Definition of done

- [ ] Timecodes unveraendert over all Sprachen (at reiner Uebersetzung)
- [ ] no negativen or null Dauern
- [ ] CPS and Zeilenlaenge im vereinbarten Rahmen (Stichprobe)
- [ ] MT as Entwurf gekennzeichnet
- [ ] Hard-Burn only with schriftlicher approval

## Security

- Vertrauliche Video-Inhalte not an oeffentliche MT-APIs without Vertrag.
- YouTube-transcripte: Nutzungsrechte am Video observe.

## Pitfalls

- Uebersetzung ganzer Bloecke verschiebt implizit Timing—cueweise arbeiten.
- mov_text not viaall; Web oft VTT separat.
- Whisper on falscher Sprache → Garbage—`language` setzen or auto verify.
- youtube-content liefert Platzhalter-Beispiele in Doku—echtes Video testen.
- Burn-in with falscher Aufloesung—subs before on safe margin verify.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** DE SRT → EN Entwurf, gleiche Cues.
- **Input:** `training_de.srt` (84 cues).
- **Prompt:**

```text
Translate cues to English, keep timecodes, mark draft, export training_en.srt.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.1
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
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Stream #0:2(ger): Subtitle: mov_text (ger)
Video codec unchanged: h264
Output: course_de_soft.mp4
```