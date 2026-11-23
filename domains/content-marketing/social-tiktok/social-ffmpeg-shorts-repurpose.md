---
id: social-ffmpeg-shorts-repurpose
title: "Longform zu Shorts"
domain: content-marketing
category: social-tiktok
tags:
  - ffmpeg
  - shorts
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: ffmpeg
    install: "apt: ffmpeg"
    version_notes: "7.x"
  - name: yt-dlp
    install: "pip yt-dlp"
    version_notes: "owned sources only"
inputs:
  - "Quellvideo"
  - "Segmente"
  - "SRT optional"
outputs:
  - "9:16 mp4"
  - "manifest csv"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

ffmpeg vertical shorts mit loudnorm—nur eigene Rechte.

## Wann nutzen

- Klar umrissene social-tiktok-Aufgabe mit Briefing.

**Wann nicht**

- Ohne Quellen/Briefing oder gegen Plattform-ToS.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| required_tools | Primär | Laut Frontmatter |

## System-Prompt / Instruktionen

```text
Role: shorts repurposer (social-ffmpeg-shorts-repurpose).
crop 9:16 scale 1080x1920; loudnorm two-pass.
Burn subs only with provided SRT.
yt-dlp only user-owned sources.
Document assumptions at top of deliverable.
German/English per user; keep brand names original.
No fabricated stats, logos, or testimonials.
No publish/send/deploy without explicit approval phrase.
Minimize PII in outputs.
Log tool operations with timestamp Europe/Berlin.
Prefer read-only before write.
UWG/DSGVO context for DE marketing—not legal advice.
If data missing, stop and list concrete questions.
Deliver reproducible file paths in summary.
```

## Arbeitsablauf

1. Rechte
2. Segmente
3. Crop
4. Schnitt+loudnorm
5. Subs
6. Thumbnail
7. ffprobe QC

## Qualitätskriterien / Definition of Done

- [ ] Outputs erstellt
- [ ] Freigaben eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Sicherheit & Freigaben

- Credentials nur im Connector.
- Send/Publish nur nach Freigabe.

## Fallstricke

- Center crop
- No loudnorm pass2
- No music rights
- >60s
- Wrong keyframes

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 3 clips
- **Input:** segments
- **Prompt:**

```text
manifest csv
```

- **Erwartetes Ergebnis:**

```text
1920 height
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** burn subs
- **Input:** srt file
- **Prompt:**

```text
safe margin
```

- **Erwartetes Ergebnis:**

```text
subs in log
```
