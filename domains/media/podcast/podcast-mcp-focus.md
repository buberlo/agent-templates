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
  - "Shorthand-Briefing (Shownotes, Kapitel, Distribution)"
outputs:
  - "Master-Audio and transcript"
  - "Entwurf Shownotes with Timestamps"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Podcast-episode of **Rohaudio** over **Mastering (FFmpeg)**, **transcript (Whisper-Skill)** bis **Shownotes-Entwurf**—MCP/Skills only dort, wo sie Transcription or Textableitung beschleunigen, not for triviale Cute.

## When to use

- Gleicher Workflow jede Woche: Master → transcript → Kapitel → Shownotes-Review.
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
| Hermes youtube-content | Referenzclips | transcripte for erwaehnte Links |
| Editor (Markdown) | Shownotes | Mensch gibt finale approval |

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
4. Kapitelliste from Segment-Timestamps per Skript or Agent-Heuristik.
5. `show_notes_draft.md` with Summary, Kapiteln, Links.
6. Host-Review-Punkte in Checkliste; no RSS-Aktion.
7. after approval: finale MP3-ID3 only with gelieferten Metadaten.

## Definition of done

- [ ] Master-LUFS im Targetkorridor
- [ ] transcript deckt >95 % the Sprechdauer ab (Stichprobe)
- [ ] Kapitelzeiten monoton; erste Kapitelmarke at 0:00 or Intro-Ende
- [ ] Shownotes as Entwurf gekennzeichnet
- [ ] no Distribution without approval

## Security

- Gaeste: Aufnahme- and Veroeffentlichungsrecht before Shownotes with Zitaten clarify.
- Whisper-Skill: Audio not an unbekannte Dritt-Endpoints when Skill cloud-nah konfiguriert—Policy read.

## Pitfalls

- transcript on komprimiertem MP3 → schlechtere ASR; immer Master-WAV.
- Kapitel from Halluzination statt Timestamps—an Transcript binden.
YouTube content for your own episode instead of file—wrong source.
- Doppeltes loudnorm on bereits mastered File of Gastgeber.
- Shownotes with ungeprueften Affiliate-Links.

## Basic examples

### Example 1 (Example data)

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
08:12 Was ist eine gute API-Grenze?
...
Files: ep42.mp3, ep42.txt, show_notes_draft.md
```

### Example 2 (Example data)

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