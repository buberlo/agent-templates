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
  - "Lyrics-Entwurf or Thema"
  - "approval for generative Musik ja/nein"
outputs:
  - "Lyrics- and Prompt-Paket"
  - "Rechte-/ToS-Checkliste"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

**Musik-Creative** strukturieren: Lyrics after Handwerksregeln, **Suno- or Diensle-Prompts** from the Hermes-Skill ableiten—generative Generierung only after Rechte-approval, no stillen Uploads.

## When to use

- Jingle, Podcast-Intro-Musik or Demo-Song geplant.
- Texte and Prompts sollen reviewbar in Markdown liegen.
- User will Skill-Wissen to Songwriting nutzen.

**When not to use**

- Mastering fertiger Multitracks (audio-editing-Template).
- Sampling urheberrechtlich geschuetzter Masters.
- Automatische Spotify-Distribution without Label-approval.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes songwriting-and-ai-music | Struktur, Prompts | Bundled Skill-catalog |
| Suno o. ae. | Generierung | only after approval; ToS variieren |
| ffmpeg | Kurz-Snippet verify | when User MP3 liefert |

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
3. Lyrics-Entwurf with klarer Struktur (Verse/Chorus).
4. Suno-Prompt bauen; Negativliste ergaenzen.
5. Rechte-Checkliste fill (ToS, territory, exclusivity).
6. User-approval einholen before Generierung.
7. Falls MP3 geliefert: `ffprobe` and Ablage document.

## Definition of done

- [ ] Lyrics strukturiert and reviewbar
- [ ] Prompt unter Plattform-Limits
- [ ] Commercial-Checkliste ausgefuellt
- [ ] no generative API without approval
- [ ] no kopierten Hook-Zeilen bekannter Hits

## Security

- Generative Musik-ToS the Anbieters before Kundenprojekt read.
- no API-Keys im Chat.

## Pitfalls

- Suno-Style-Prompt with Kuenstlernamen → Ablehnung or rechtliches Risiko.
- Lyrics in falscher Sprache for Vocal-Model.
- Commercial=Yes without Pro-Plan according to Anbieter.
- to langer Prompt will abgeschnitten—Prioritaeten vorne.
- Skill-Example 1:1 as Kundenlyrics kopieren.

## Basic examples

### Example 1 (Example data)

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

### Example 2 (Example data)

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
jede Ecke ein Versprechen — ich lass mich rein.
```