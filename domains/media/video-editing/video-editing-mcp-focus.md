---
id: video-editing-mcp-focus
title: "Video-Editing: FFmpeg-CLI vs. Skills"
domain: media
category: video-editing
tags:
  - video
  - ffmpeg
  - mcp
  - skills
target_agents:
  - hermes
  - generic-mcp-agents
  - cursor
required_tools:
  - name: ffmpeg
    install: "OS-Paket ffmpeg"
    version_notes: "Primaerer path; MCP oft viafluessig"
  - name: Remotion Agent Skills
    install: "https://github.com/remotion-dev/skills"
    version_notes: "for Motion/Code-Videos statt Timeline-MCP"
  - name: Hermes-Skill Video Frames
    install: "ClawHub Video Frames (steipete) at OpenClaw"
    version_notes: "Frame-Extraktion; only when required"
inputs:
  - "Video-Task (Cut, Conversion, Frames, Motion)"
  - "List of allowed tools/MCPs"
outputs:
  - "Ausgefuehrte Befehle or gerenderter Clip"
  - "Empfehlung CLI vs. MCP with Begruendung"
risk_level: low
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Agents choose the **lightest reliable path** for video tasks: usually **FFmpeg in the terminal**, skills for Remotion or frame extraction—MCP only when there is real added value over the token overhead.

## When to use

- Task laesst sich as ein or wenige FFmpeg-Befehle formulieren.
- Motion Graphics or datengetriebene Clips → Remotion Skills.
- Einzelbilder from Video for QA or Thumbnail.

**When not to use**

- Komplexe Multi-Track-Timeline with J-Cuts and Sounddesign in NLE.
- Do not load the MCP catalog “completely” without a task reference (context cost).
- Live-OBS-Produktion.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| ffmpeg / ffprobe | Cut, Encode, Metadaten | no MCP required; Hermes Video-Analyse setzt PATH voraus |
| Remotion Skills | React-Video | Official 2026-path statt Legacy-MCP |
| Video Frames Skill | Stills | OpenClaw/ClawHub; only at Bedarf |
| youtube-content skill | Transcript→text | When output is text, not re-encode |

## System prompt

```text
You plan and execute video tasks with minimal tool surface area.

Decision tree:
1) If the user needs cut/transcode/normalize/subtitle mux → use ffmpeg/ffprobe via shell; do not spin up a video MCP for a single command.
2) If the output is programmatic motion graphics or data-driven slides → use Remotion skills and TypeScript, not an NLE MCP.
3) If the user needs still frames at timestamps → prefer ffmpeg -ss -frames:v 1; use Video Frames skill only if already in the agent policy.
4) If the user needs transcript or chapters from YouTube → use youtube-content skill; do not re-download video unless requested.

For any MCP: quote estimated token/schema overhead; prefer include/exclude filters (Hermes, OpenClaw policy).

Always document: chosen path, rejected alternatives, commands run, output paths.

Verify with ffprobe after encode. Seek approval before uploads, burn-in subs, or destructive overwrites.

When unsure between copy and re-encode, probe codecs and explain tradeoff to the user in one paragraph.

Include a one-line risk note if source is ProRes/DNx and target is web H.264 (generation loss expected).
If user requests YouTube clip only as audio reference, separate text skill from file pipeline.
Escalate to human editor when requested deliverable mentions color grade or multitrack mix.
Prefer stream copy for mezzanine archives when user asks for lossless interim only.
Log wall-clock time for ffmpeg jobs exceeding five minutes for capacity planning.
```

## Workflow

1. Task klassifizieren: file-Op vs. Generativ vs. Text from Video.
2. Tool-Policy verify: unrequirede MCPs disable.
3. `ffprobe` on input file; define cut profile.
4. FFmpeg-Befehl ausfuehren or Remotion-Render starten.
5. Verify output with `ffprobe` and a frame grab if needed.
6. Kurzbericht: warum no MCP / welches Skill genutzt.
7. at catalog-pathen: Link to remotion-dev/skills or ffmpeg.org notieren.

## Definition of done

- [ ] Geringstpossiblee Tool-Menge aktiv
- [ ] Befehle reproduzierbar dokumentiert
- [ ] no MCP only for `ffmpeg -version`
- [ ] Output technisch geprueft
- [ ] approvaln at Publish/Overwrite eingehalten

## Security

- MCP-Credentials not in argv; OAuth on Connector-Backend (Grok-Bot-Wiki).
- Video with personal data: process locally only whenever possible.

## Pitfalls

- MCP-Schema-Overhead kann Zehntausende Tokens kosten—before messen/policy.
- Fragmented FFmpeg MCPs without a clear maintainer—prefer the CLI.
- Skills vs. MCP verwechseln: Skills are Procedures, no Socket-Verbindung.
- Remotion without Skills → veraltete MCP-Namen in aelteren Threads.
- Frame skill vs. ffmpeg: duplicate work costs time and context.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 30 s Teaser from Webinar extract.
- **Input:** `webinar.mkv`, 01:12:00 total, Ausschnitt ab 00:45:10.
- **Prompt:**

```text
Use ffmpeg only: cut 30s from 00:45:10, 1080p H.264 faststart. Explain why no video MCP.
```

- **Expected result:**

```bash
ffmpeg -ss 00:45:10 -i webinar.mkv -t 30 -vf scale=-2:1080 -c:v libx264 -crf 22 -c:a aac -movflags +faststart teaser.mp4
Rationale: single-pass transcode; MCP adds no capability.
```

### Example 2 (Example data (self-written))
- **Task:** MCP-Token-Overhead deliberately vermeiden.
- **Input:** Policy allows only terminal + ffmpeg.
- **Prompt:**

```text
Plan webinar cut but load zero video MCPs; cite r/ClaudeAI MCP overhead discussion if user asks about MCP.
```

- **Expected result:**

  Plan with reinen Shell-commands; Verweis https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/ ; no MCP-Toolcall in the Ausfuehrung.