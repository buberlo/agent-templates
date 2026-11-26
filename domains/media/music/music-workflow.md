---
id: music-workflow
title: "Songwriting and AI-Musik-Prompts"
domain: media
category: music
tags:
  - music
  - songwriting
  - suno
target_agents:
  - hermes
  - openclaw
  - generic
required_tools:
  - name: Hermes-Skill songwriting-and-ai-music
    install: "Bundled creative/songwriting-and-ai-music"
    version_notes: "Craft + Suno-Prompt-Patterns"
inputs:
  - "Mood, Genre, Tempo, Sprache"
  - "Lyrics draft or theme"
  - "approval for generative Musik ja/nein"
outputs:
  - "Lyrics- and Prompt-Paket"
  - "Rights/ToS checklist"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Structure **music creative** work: craft lyrics by songwriting rules and derive **Suno or service prompts** from the Hermes skill—run generative creation only after rights approval, with no silent uploads.

## When to use

- Jingle, Podcast-Intro-Musik or Demo-Song geplant.
- Lyrics and prompts should be stored in Markdown for review.
- User will Skill-Wissen to Songwriting nutzen.

**When not to use**

- Mastering fertiger Multitracks (audio-editing-Template).
- Sampling copyrighted masters.
- Automatische Spotify-Distribution without Label-approval.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes songwriting-and-ai-music | Struktur, Prompts | Bundled Skill-catalog |
| Suno o. ae. | Generierung | only after approval; ToS variieren |
| ffmpeg | Verify short snippet | When user provides MP3 |

## System prompt

```text
You help with songwriting craft and AI music generation prompts; you do not submit to Suno or other services without explicit user approval.

Inputs: genre, bpm range, mood, language, section structure (verse/chorus/bridge), reference artists (style only, no copying), lyrics seed or theme, commercial use (yes/no).

Lyrics workflow:
- Propose title, hook, and structure with syllable-aware lines for the stated genre.
- Mark rhyme scheme; offer one alternate hook.
- Flag clichés and suggest concrete imagery.

AI music prompt (Suno-style):
- Combine genre tags, tempo, instrumentation, vocal gender/style, negative constraints (no shout, no lengthy intro).
- Keep prompts under platform limit; split style vs lyrics fields as platform expects.

Legal:
- Remind user that generative outputs may have restricted commercial rights per provider ToS.
- No copyrighted melody replication; style influence only.

If user supplies generated mp3: ffprobe duration and bitrate; no upload elsewhere.

Deliver: lyrics.md, suno_prompt.txt, checklist_commercial.md, optional revision notes.

Never spend credits or call paid APIs without confirmation.
```

## Workflow

1. Briefing: Genre, Mood, Commercial ja/nein.
2. Skill-README for Prompt-Muster oeffnen.
3. Lyrics draft with a clear structure (verse/chorus).
4. Suno-Prompt bauen; Negativliste ergaenzen.
5. Fill out rights checklist (ToS, territory, exclusivity).
6. User-approval einholen before Generierung.
7. If MP3 provided: run `ffprobe` and document storage location.

## Definition of done

- [ ] Lyrics structured and ready for review
- [ ] Prompt within platform limits
- [ ] Commercial checklist completed
- [ ] no generative API without approval
- [ ] no kopierten Hook-Zeilen bekannter Hits

## Security

- Generative Musik-ToS the Anbieters before Kundenprojekt read.
- No API keys in chat.

## Pitfalls

- Suno-Style-Prompt with Kuenstlernamen → Ablehnung or rechtliches Risiko.
- Lyrics in the wrong language for the vocal model.
- Commercial=Yes without Pro-Plan according to Anbieter.
- to langer Prompt will abgeschnitten—Prioritaeten vorne.
- Skill-Example 1:1 as Kundenlyrics kopieren.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 30 s Podcast-Intro, instrumental, uptempo.
- **Input:** Funk, 110 BPM, no Vocals.
- **Prompt:**

```text
Draft Suno-style prompt for 30s instrumental podcast intro; lyrics N/A; include negative: vocals, long buildup.
```

- **Expected result:**

```text
Style: funky, 110 bpm, tight drums, bass guitar, brass stabs, 30 second structure, radio ready
Negative: vocals, ambient pad, slow intro
Checklist: commercial_use pending user ToS review
```

### Example 2 (Example data (self-written))
- **Task:** Chorus for deutschsprachigen Pop-Song.
- **Input:** Thema „Ankommen in neuer Stadt“.
- **Prompt:**

```text
Write chorus 4 lines DE, catchy hook, suggest title; no generative call.
```

- **Expected result:**

```markdown
**Title:** New Streets
**Chorus:**
Lichter wie Konfetti, ich atme dich ein,
every corner a promise — I let myself in.
```