---
id: youtube-content-workflow
domain: medien
title: "YouTube-Transkript zu Kapiteln und Content"
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
  - "YouTube-URL oder Video-ID"
  - "Gewünschtes Format (Summary, Kapitel, Thread, Blog)"
outputs:
  - "Text-Artefakt mit Timestamps"
  - "Hinweise wenn Transkript fehlt"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Aus **öffentlichen YouTube-Videos** strukturierten **Text-Content** erzeugen—Kapitel, Summary, Zitate—mit Hermes **youtube-content** Skill, chunking bei langen Transkripten und ohne Halluzination bei fehlenden Untertiteln.

## Wann nutzen

- Kanal- oder Research-Video soll Blogpost, Newsletter oder internes Briefing werden.
- Transkript ist verfügbar oder auto-generated auf YouTube.
- Hermes-Skill mit vorbereitetem venv nutzbar.

**Wann nicht**

- Video herunterladen oder reuploaden ohne Lizenz.
- Inhalte mit deaktivierten Transkripten und ohne Freigabe für ASR-Download.
- Echtzeit-Trending ohne URL.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Hermes youtube-content | Transkript + Formate | Offizieller bundled Pfad |
| YouTube Watcher Skill | Monitoring | OpenClaw-Alternative |
| Markdown/Office-Skills | Ausgabe-Dateien | Blog/Deck optional |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. URL validieren; Video-ID extrahieren.
2. Skill: Transkript mit Timestamps holen; leere Antwort → Abbruch melden.
3. Zeichenzahl prüfen; ggf. chunken.
4. Format laut Auftrag erzeugen (Default Summary wenn unklar).
5. Timestamps stichprobenartig gegen Transkript-Zeilen.
6. `output.md` schreiben; Quell-URL im Footer.
7. Nutzer um Freigabe für externe Veröffentlichung bitten.

## Qualitätskriterien / Definition of Done

- [ ] Keine Inhalte bei fehlendem Transkript
- [ ] Kapitel-Timestamps aus echten Cues
- [ ] Zitate wortgetreu
- [ ] Quell-URL dokumentiert
- [ ] Skill-Doku-Platzhalter nicht als Ergebnis ausgegeben

## Sicherheit & Freigaben

- Urheberrecht und YouTube-ToS bei Weiterverwertung beachten.
- Keine Umgehung von Age-Gate oder Paywall.

## Fallstricke

- Auto-Untertitel fehlerhaft bei Fachjargon—Review markieren.
- >50k Zeichen ohne Chunking → Context-Overflow.
- Skill-Beispiele in Doku als echtes Output kopieren—verboten.
- YouTube Watcher und youtube-content doppelt → redundante API-Last.
- Thread-Format überschreitet Zeichenlimits ohne Split.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Kapitel + Kurzsummary für Tutorial-URL.
- **Input:** `https://www.youtube.com/watch?v=dQw4w9WgXcQ` (Beispiel-ID), Format Kapitel.
- **Prompt:**

```text
/youtube-content chapters + 8-sentence summary for URL; abort if no transcript.
```

- **Erwartetes Ergebnis:**

```markdown
## Kapitel
00:00 Einführung
02:14 Setup-Schritt
...

## Summary
… (8 Sätze mit Quellenbezug)

Quelle: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### Beispiel 2 (Praxisbeispiel)

- **Aufgabe:** Langes Interview chunken.
- **Input:** Transkript 72k Zeichen.
- **Prompt:**

```text
Chunk at 50k per skill guidance, merge blog outline with consistent H2, preserve timestamps.
```

- **Erwartetes Ergebnis:**

```text
Chunks: 2
Sections: 14 H2 mit timestamps
No placeholder text from skill readme
```