---
id: youtube-content-workflow
title: "YouTube Transcript to Chapters and Content"
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
  - "Desired format (summary, chapters, thread, blog)"
outputs:
  - "Text-Artefakt with Timestamps"
  - "Hinweise when transcript fehlt"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Create structured **text content** from **public YouTube videos**—chapters, summary, quotes—with the Hermes **youtube-content** skill, chunking for long transcripts, and without hallucination when subtitles are missing.

## When to use

- Kanal- or Research-Video should Blogpost, Newsletter or internes Briefing will.
- Transcript is available or auto-generated on YouTube.
- Hermes-Skill with vorbereitetem venv nutzbar.

**When not to use**

- Video herunterladen or reuploaden without Lizenz.
- Content with disabled transcripts and without approval for ASR download.
- Echtzeit-Trending without URL.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Hermes youtube-content | transcript + Formate | Official bundled path |
| YouTube Watcher Skill | Monitoring | OpenClaw-Alternative |
| Markdown/Office skills | Output files | Blog/deck optional |

## System prompt

```text
You derive written content from YouTube videos using the youtube-content skill workflow.

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
Attribute source URL in every deliverable footer.
```

## Workflow

1. URL validieren; Video-ID extract.
2. Skill: transcript with Timestamps holen; leere Antwort → Abbruch melden.
3. Verify character count; chunk if necessary.
4. Format according to Auftrag create (Default Summary when unklar).
5. Spot-check timestamps against transcript lines.
6. `output.md` write; Quell-URL im Footer.
7. Ask user for approval before external publication.

## Definition of done

- [ ] No content generated when transcript is missing
- [ ] Chapter timestamps from real cues
- [ ] Zitate wortgetreu
- [ ] Source URL documented
- [ ] Skill-Doku-Platzhalter not as result ausgegeben

## Security

- copyright and YouTube-ToS at Weiterverwertung observe.
- no Umgehung of Age-Gate or Paywall.

## Pitfalls

- Auto-Subtitles fehlerhaft at Fachjargon—Review markieren.
- >50k characters without chunking → context overflow.
- Copying skill examples in docs as real output—prohibited.
- Duplicate YouTube Watcher and youtube-content → redundant API load.
- Thread format exceeds character limits without splitting.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Chapters + short summary for tutorial URL.
- **Input:** `https://www.youtube.com/watch?v=dQw4w9WgXcQ` (example ID), chapters format.
- **Prompt:**

```text
/youtube-content chapters + 8-sentence summary for URL; abort if no transcript.
```

- **Expected result:**

```markdown
## Chapters
00:00 Introduction
02:14 Setup step
...

## Summary
… (8 sentences with source references)

Source: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Example 2 (Example data (self-written))
- **Task:** Chunk a long interview.
- **Input:** transcript 72k characters.
- **Prompt:**

```text
Chunk at 50k per skill guidance, merge blog outline with consistent H2, preserve timestamps.
```

- **Expected result:**

```text
Chunks: 2
Sections: 14 H2 with timestamps
No placeholder text from skill readme
```