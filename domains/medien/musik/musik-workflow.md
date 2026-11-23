---
id: musik-workflow
domain: medien
title: "Songwriting und AI-Musik-Prompts"
category: musik
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
  - "Lyrics-Entwurf oder Thema"
  - "Freigabe für generative Musik ja/nein"
outputs:
  - "Lyrics- und Prompt-Paket"
  - "Rechte-/ToS-Checkliste"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

**Musik-Creative** strukturieren: Lyrics nach Handwerksregeln, **Suno- oder Diensle-Prompts** aus dem Hermes-Skill ableiten—generative Generierung nur nach Rechte-Freigabe, keine stillen Uploads.

## Wann nutzen

- Jingle, Podcast-Intro-Musik oder Demo-Song geplant.
- Texte und Prompts sollen reviewbar in Markdown liegen.
- Nutzer will Skill-Wissen zu Songwriting nutzen.

**Wann nicht**

- Mastering fertiger Multitracks (audio-bearbeitung-Template).
- Sampling urheberrechtlich geschützter Masters.
- Automatische Spotify-Distribution ohne Label-Freigabe.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes songwriting-and-ai-music | Struktur, Prompts | Bundled Skill-Katalog |
| Suno o. ä. | Generierung | Nur nach Freigabe; ToS variieren |
| ffmpeg | Kurz-Snippet prüfen | Wenn User MP3 liefert |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Briefing: Genre, Mood, Commercial ja/nein.
2. Skill-README für Prompt-Muster öffnen.
3. Lyrics-Entwurf mit klarer Struktur (Verse/Chorus).
4. Suno-Prompt bauen; Negativliste ergänzen.
5. Rechte-Checkliste ausfüllen (ToS, territory, exclusivity).
6. Nutzer-Freigabe einholen vor Generierung.
7. Falls MP3 geliefert: `ffprobe` und Ablage dokumentieren.

## Qualitätskriterien / Definition of Done

- [ ] Lyrics strukturiert und reviewbar
- [ ] Prompt unter Plattform-Limits
- [ ] Commercial-Checkliste ausgefüllt
- [ ] Keine generative API ohne Freigabe
- [ ] Keine kopierten Hook-Zeilen bekannter Hits

## Sicherheit & Freigaben

- Generative Musik-ToS des Anbieters vor Kundenprojekt lesen.
- Keine API-Keys im Chat.

## Fallstricke

- Suno-Style-Prompt mit Künstlernamen → Ablehnung oder rechtliches Risiko.
- Lyrics in falscher Sprache für Vocal-Model.
- Commercial=Yes ohne Pro-Plan laut Anbieter.
- Zu langer Prompt wird abgeschnitten—Prioritäten vorne.
- Skill-Beispiel 1:1 als Kundenlyrics kopieren.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 30 s Podcast-Intro, instrumental, uptempo.
- **Input:** Funk, 110 BPM, keine Vocals.
- **Prompt:**

```text
Draft Suno-style prompt for 30s instrumental podcast intro; lyrics N/A; include negative: vocals, long buildup.
```

- **Erwartetes Ergebnis:**

```text
Style: funky, 110 bpm, tight drums, bass guitar, brass stabs, 30 second structure, radio ready
Negative: vocals, ambient pad, slow intro
Checklist: commercial_use pending user ToS review
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Chorus für deutschsprachigen Pop-Song.
- **Input:** Thema „Ankommen in neuer Stadt“.
- **Prompt:**

```text
Write chorus 4 lines DE, catchy hook, suggest title; no generative call.
```

- **Erwartetes Ergebnis:**

```markdown
**Titel:** Neue Straßen
**Chorus:**
Lichter wie Konfetti, ich atme dich ein,
jede Ecke ein Versprechen — ich lass mich rein.
```