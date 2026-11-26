---
id: podcast-mcp-focus
title: "Podcast-Produktion: CLI, Whisper and Skills"
domain: media
category: podcast
tags:
  - podcast
  - whisper
  - ffmpeg
  - shownotes
target_agents:
  - hermes
  - openclaw
  - generic-mcp-agents
required_tools:
  - name: ffmpeg
    install: "OS-Paket ffmpeg"
    version_notes: "Cut, loudnorm, concat"
  - name: OpenClaw Skill OpenAI Whisper
    install: "openclaw skills install (steipete, Openai Whisper)"
    version_notes: "ClawHub ~77k Downloads (Stand Recherche 2026-11)"
  - name: Hermes-Skill youtube-content
    install: "Bundled media-youtube-content"
    version_notes: "for Clip-Recherche/transcripte externer Videos"
inputs:
  - "Episoden-Rohmaterial or fertige WAV/MP3"
  - "Shorthand briefing (show notes, chapters, distribution)"
outputs:
  - "Master-Audio and transcript"
  - "Draft shownotes with timestamps"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Podcast episode from **raw audio** through **mastering (FFmpeg)**, **transcript (Whisper skill)** to **draft show notes**—use MCP/skills only where they speed up transcription or text derivation, not for trivial cuts.

## When to use

- Same workflow every week: master → transcript → chapters → show notes review.
- OpenClaw/Hermes with Whisper-Skill bereits freigeschaltet.
- distribution erfolgt manuell or in separatem step.

**When not to use**

- Vollautomatischer RSS-Push and Spotify-Upload without menschliche Kontrolle.
- Musik-Podcast with Stem-Mastering in DAW.
Pure marketing campaigns without audio source.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| ffmpeg | Master, Cut Filler | CLI, datensparsam |
| Whisper Skill | transcript | Haeufig installiert on ClawHub |
| Hermes youtube-content | Reference clips | Transcripts for mentioned links |
| Editor (Markdown) | Show notes | Human gives final approval |

## System prompt

```text
You support podcast post-production: audio mastering via ffmpeg, transcription via approved Whisper skill, and draft show notes.

Inputs: episode audio path, target loudness (-16 LUFS default), intro/outro files optional, episode title and guest names, links to mention, language for ASR.

Order of operations:
1) Master audio with two-pass loudnorm; do not publish.
2) Run Whisper skill on mastered WAV (not lossy MP3) for best ASR.
3) From transcript, propose chapter markers every 3-7 minutes at natural breaks; format HH:MM:SS for podcast hosts.
4) Draft show notes: summary (120 words), bullet takeaways, linked resources, chapter list.
5) Flag proper nouns ASR got wrong for human fix.

Skills vs MCP: use Whisper skill procedure; do not add unrelated MCP servers.

Never push to Spotify, Apple, or RSS URLs without explicit approval.
Quotes and controversial statements: mark for host legal review, do not auto-approve.

Output bundle: mastered mp3 path, transcript .txt/.srt, show_notes_draft.md, command log.

Align chapter titles with spoken transitions; avoid generic labels like "Part 2".
If episode mentions URLs, verify they resolve with HEAD request before show notes.
Distinguish sponsor segments in notes when user marks ad reads in briefing.
```

## Workflow

1. Rohaudio annehmen; `ffprobe` for Dauer/Peaks.
2. Two-pass `loudnorm` → `episode_master.wav` (siehe Template audio-ffmpeg-podcast-master).
3. Whisper-Skill on Master-WAV; Output in `transcript/`.
4. Chapter list from segment timestamps via script or agent heuristic.
5. `show_notes_draft.md` with summary, chapters, links.
6. Host review items in checklist; no RSS action.
7. after approval: finale MP3-ID3 only with gelieferten Metadaten.

## Definition of done

- [ ] Master-LUFS im Targetkorridor
- [ ] Transcript covers >95% of speaking duration (spot check)
- [ ] Chapter times monotonic; first chapter marker at 0:00 or end of intro
- [ ] Show notes marked as draft
- [ ] no Distribution without approval

## Security

- Guests: clarify recording and publication rights before publishing show notes with quotes.
- Whisper-Skill: Audio not an unbekannte Dritt-Endpoints when Skill cloud-nah konfiguriert—Policy read.

## Pitfalls

- transcript on komprimiertem MP3 → schlechtere ASR; immer Master-WAV.
- Chapters from hallucination instead of timestamps—bind to transcript.
YouTube content for your own episode instead of file—wrong source.
- Double loudnorm on an already mastered file from the host.
- Shownotes with ungeprueften Affiliate-Links.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** episode 42: Master + DE-transcript.
- **Input:** `ep42_raw.wav`, Titel „API-Design with Lea“.
- **Prompt:**

```text
Master to -16 LUFS MP3, Whisper DE transcript, draft show notes with 4 chapters.
```

- **Expected result:**

```markdown
## Ep42 – API design with Lea (DRAFT)
00:00 Intro
08:12 What is a good API boundary?
...
Files: ep42.mp3, ep42.txt, show_notes_draft.md
```

### Example 2 (Example data (self-written))
- **Task:** Eigennamen after ASR korrigieren.
- **Input:** transcript with „Graph QL“ statt „GraphQL“.
- **Prompt:**

```text
List proper-noun fixes for host approval before publishing show notes; do not auto-replace in final RSS text.
```

- **Expected result:**

| Stelle | ASR | Vorschlag |
|--------|-----|-----------|
| 00:12:04 | Graph QL | GraphQL |
| 00:34:18 | Kubernetis | Kubernetes |