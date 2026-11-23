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

## Purpose

ffmpeg vertical shorts with loudnorm—own rights only.

## When to use

- Clearly outlined social-tiktok task with briefing.

**When not to use**

- Without sources/briefing or against platform-ToS.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| required tools | Primary | According to Frontmatter |

## System prompt

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

## Workflow

1. Rechte
2. Segmente
3. Crop
4. Schnitt+loudnorm
5. Subs
6. Thumbnail
7. ffprobe QC

## Definition of done

- [ ] Outputs erstellt
- [ ] user approvaln eingehalten
- [ ] Quellen/Annahmen geloggt
- [ ] Kein Auto-Publish

## Security

- Credentials nur im Connector.
- Send/Publish only after release.

## Pitfalls

- Center crop
- No loudnorm pass2
- No music rights
- >60s
- Wrong keyframes

## Basic examples

### Example 1 (Example data)

- **Task:** 3 clips
- **Input:** segments
- **Prompt:**

```text
manifest csv
```

- **Expected result:**

```text
1920 height
```

### Example 2 (Example data)

- **Task:** burn subs
- **Input:** srt file
- **Prompt:**

```text
safe margin
```

- **Expected result:**

```text
subs in log
```
