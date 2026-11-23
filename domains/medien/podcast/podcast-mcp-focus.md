---
id: podcast-mcp-focus
domain: medien
title: "Podcast-Produktion: CLI, Whisper und Skills"
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
    version_notes: "Schnitt, loudnorm, concat"
  - name: OpenClaw Skill OpenAI Whisper
    install: "openclaw skills install (steipete, Openai Whisper)"
    version_notes: "ClawHub ~77k Downloads (Stand Recherche 2026-11)"
  - name: Hermes-Skill youtube-content
    install: "Bundled media-youtube-content"
    version_notes: "Für Clip-Recherche/Transkripte externer Videos"
inputs:
  - "Episoden-Rohmaterial oder fertige WAV/MP3"
  - "Shorthand-Briefing (Shownotes, Kapitel, Distribution)"
outputs:
  - "Master-Audio und Transkript"
  - "Entwurf Shownotes mit Timestamps"
risk_level: medium
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Podcast-Folge von **Rohaudio** über **Mastering (FFmpeg)**, **Transkript (Whisper-Skill)** bis **Shownotes-Entwurf**—MCP/Skills nur dort, wo sie Transkription oder Textableitung beschleunigen, nicht für triviale Schnitte.

## Wann nutzen

- Gleicher Workflow jede Woche: Master → Transkript → Kapitel → Shownotes-Review.
- OpenClaw/Hermes mit Whisper-Skill bereits freigeschaltet.
- Verteilung erfolgt manuell oder in separatem Schritt.

**Wann nicht**

- Vollautomatischer RSS-Push und Spotify-Upload ohne menschliche Kontrolle.
- Musik-Podcast mit Stem-Mastering in DAW.
- Reine Marketing-Kampagne ohne Audio-Quelle.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ffmpeg | Master, Schnitt Filler | CLI, datensparsam |
| Whisper Skill | Transkript | Häufig installiert auf ClawHub |
| Hermes youtube-content | Referenzclips | Transkripte für erwähnte Links |
| Editor (Markdown) | Shownotes | Mensch gibt finale Freigabe |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Rohaudio annehmen; `ffprobe` für Dauer/Peaks.
2. Two-pass `loudnorm` → `episode_master.wav` (siehe Template audio-ffmpeg-podcast-master).
3. Whisper-Skill auf Master-WAV; Output in `transcript/`.
4. Kapitelliste aus Segment-Timestamps per Skript oder Agent-Heuristik.
5. `show_notes_draft.md` mit Summary, Kapiteln, Links.
6. Host-Review-Punkte in Checkliste; keine RSS-Aktion.
7. Nach Freigabe: finale MP3-ID3 nur mit gelieferten Metadaten.

## Qualitätskriterien / Definition of Done

- [ ] Master-LUFS im Zielkorridor
- [ ] Transkript deckt >95 % der Sprechdauer ab (Stichprobe)
- [ ] Kapitelzeiten monoton; erste Kapitelmarke bei 0:00 oder Intro-Ende
- [ ] Shownotes als Entwurf gekennzeichnet
- [ ] Keine Distribution ohne Freigabe

## Sicherheit & Freigaben

- Gäste: Aufnahme- und Veröffentlichungsrecht vor Shownotes mit Zitaten klären.
- Whisper-Skill: Audio nicht an unbekannte Dritt-Endpoints wenn Skill cloud-nah konfiguriert—Policy lesen.

## Fallstricke

- Transkript auf komprimiertem MP3 → schlechtere ASR; immer Master-WAV.
- Kapitel aus Halluzination statt Timestamps—an Transcript binden.
- youtube-content für eigene Episode statt Datei—falsche Quelle.
- Doppeltes loudnorm auf bereits mastered File von Gastgeber.
- Shownotes mit ungeprüften Affiliate-Links.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Folge 42: Master + DE-Transkript.
- **Input:** `ep42_raw.wav`, Titel „API-Design mit Lea“.
- **Prompt:**

```text
Master to -16 LUFS MP3, Whisper DE transcript, draft show notes with 4 chapters.
```

- **Erwartetes Ergebnis:**

```markdown
## Ep42 – API-Design mit Lea (ENTWURF)
00:00 Intro
08:12 Was ist eine gute API-Grenze?
...
Files: ep42.mp3, ep42.txt, show_notes_draft.md
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Eigennamen nach ASR korrigieren.
- **Input:** Transkript mit „Graph QL“ statt „GraphQL“.
- **Prompt:**

```text
List proper-noun fixes for host approval before publishing show notes; do not auto-replace in final RSS text.
```

- **Erwartetes Ergebnis:**

| Stelle | ASR | Vorschlag |
|--------|-----|-----------|
| 00:12:04 | Graph QL | GraphQL |
| 00:34:18 | Kubernetis | Kubernetes |