---
id: youtube-content-workflow
title: "YouTube-transcript to Kapiteln and Content"
domain: media
category: youtube-content
tags:
  - youtube
  - transcript
  - chapters
target_agents:
  - hermes
  - openclaw
  - generic
required_tools:
  - name: Hermes-Skill youtube-content
    install: "Bundled media-youtube-content"
    version_notes: "fetch_transcript.py via venv youtube extra"
  - name: ClawHub YouTube Watcher
    install: "openclaw skills install (michaelgathara)"
    version_notes: "Alternative Monitor/Summary"
inputs:
  - "YouTube-URL or Video-ID"
  - "Gewuenschtes Format (Summary, Kapitel, Thread, Blog)"
outputs:
  - "Text-Artefakt with Timestamps"
  - "Hinweise when transcript fehlt"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

from **oeffentlichen YouTube-Videos** structured **Text-Content** create—Kapitel, Summary, Zitate—with Hermes **youtube-content** Skill, chunking at langen transcripten and without Halluzination at fehlenden Subtitlesn.

## When to use

- Kanal- or Research-Video should Blogpost, Newsletter or internes Briefing will.
- transcript is verfuegbar or auto-generated on YouTube.
- Hermes-Skill with vorbereitetem venv nutzbar.

**When not to use**

- Video herunterladen or reuploaden without Lizenz.
- Inhalte with deaktivierten transcripten and without approval for ASR-Download.
- Echtzeit-Trending without URL.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes youtube-content | transcript + Formate | Official bundled path |
| YouTube Watcher Skill | Monitoring | OpenClaw-Alternative |
| Markdown/Office-Skills | Ausgabe-files | Blog/Deck optional |

## System prompt

```text
You derive written content from YouTube videos using the youtube-content skill workflow.

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: video URL, output format (summary|chapters|thread|blog|quotes), language preference, max length, chunking threshold (default 50000 chars).
Fetch:
- Use skill helper with --text-only --timestamps as documented.
- If transcript empty: stop and report (captions disabled, age-restricted, private); do not invent content.
Processing:
- For videos longer than chunk threshold, split transcript by timestamps, process sequentially, merge with consistent heading hierarchy.
- Chapters: align to natural topic shifts; each entry must have HH:MM:SS from transcript time base, not guessed.
- Summary: 8-12 sentences for default; cite notable timestamps in parentheses.
- Quotes: verbatim from transcript lines only; max 240 chars per quote unless user extends.
Formats:
- Thread: numbered tweets under 280 chars where possible; timestamps optional.
- Blog: markdown H2 per chapter; no fabricated expert claims.
Examples in skill docs are placeholders—never paste them as if real output.
Publishing: no posting to YouTube, X, or blogs without user approval.
Attribute source URL in every deliverable footer.```

## Workflow

1. URL validieren; Video-ID extract.
2. Skill: transcript with Timestamps holen; leere Antwort → Abbruch melden.
3. Zeichenzahl verify; ggf. chunken.
4. Format according to Auftrag create (Default Summary when unklar).
5. Timestamps stichprobenartig against transcript-Zeilen.
6. `output.md` write; Quell-URL im Footer.
7. User um approval for externe Veroeffentlichung bitten.

## Definition of done

- [ ] no Inhalte at fehlendem transcript
- [ ] Kapitel-Timestamps from echten Cues
- [ ] Zitate wortgetreu
- [ ] Quell-URL dokumentiert
- [ ] Skill-Doku-Platzhalter not as result ausgegeben

## Security

- copyright and YouTube-ToS at Weiterverwertung observe.
- no Umgehung of Age-Gate or Paywall.

## Pitfalls

- Auto-Subtitles fehlerhaft at Fachjargon—Review markieren.
- >50k Zeichen without Chunking → Context-Overflow.
- Skill-Beispiele in Doku as echtes Output kopieren—verboten.
- YouTube Watcher and youtube-content doppelt → redundante API-Last.
- Thread-Format viaschreitet Zeichenlimits without Split.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Kapitel + Kurzsummary for Tutorial-URL.
- **Input:** `https://www.youtube.com/watch?v=dQw4w9WgXcQ` (Example-ID), Format Kapitel.
- **Prompt:**

```text
/youtube-content chapters + 8-sentence summary for URL; abort if no transcript.
```

- **Expected result:**

```markdown
## Kapitel
00:00 Introduction
02:14 Setup-Schritt
...

## Summary
… (8 sentences with source references)

Source: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Example 2 (Real-world example)

- **Task:** Langes Interview chunken.
- **Input:** transcript 72k Zeichen.
- **Prompt:**

```text
Chunk at 50k per skill guidance, merge blog outline with consistent H2, preserve timestamps.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Chunks: 2
Sections: 14 H2 with timestamps
No placeholder text from skill readme
```