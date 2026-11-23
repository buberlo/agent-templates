---
id: video-bearbeitung-mcp-focus
domain: medien
title: "Video-Bearbeitung: FFmpeg-CLI vs. Skills"
category: video-bearbeitung
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
    version_notes: "Primärer Pfad; MCP oft überflüssig"
  - name: Remotion Agent Skills
    install: "https://github.com/remotion-dev/skills"
    version_notes: "Für Motion/Code-Videos statt Timeline-MCP"
  - name: Hermes-Skill Video Frames
    install: "ClawHub Video Frames (steipete) bei OpenClaw"
    version_notes: "Frame-Extraktion; nur wenn nötig"
inputs:
  - "Video-Aufgabe (Schnitt, Konvertierung, Frames, Motion)"
  - "Liste erlaubter Tools/MCPs"
outputs:
  - "Ausgeführte Befehle oder gerenderter Clip"
  - "Empfehlung CLI vs. MCP mit Begründung"
risk_level: low
version: "1.1.0"
updated: "2026-11-23"
example_count: 2
---

## Zweck

Agenten wählen den **leichtesten belastbaren Pfad** für Video-Aufgaben: meist **FFmpeg im Terminal**, Skills für Remotion oder Frame-Extraktion—MCP nur, wenn echter Mehrwert gegenüber Token-Overhead besteht.

## Wann nutzen

- Aufgabe lässt sich als ein oder wenige FFmpeg-Befehle formulieren.
- Motion Graphics oder datengetriebene Clips → Remotion Skills.
- Einzelbilder aus Video für QA oder Thumbnail.

**Wann nicht**

- Komplexe Multi-Track-Timeline mit J-Cuts und Sounddesign in NLE.
- MCP-Katalog soll ohne Aufgabenbezug „komplett“ geladen werden (Kontextkosten).
- Live-OBS-Produktion.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| ffmpeg / ffprobe | Schnitt, Encode, Metadaten | Kein MCP nötig; Hermes Video-Analyse setzt PATH voraus |
| Remotion Skills | React-Video | Offizieller 2026-Pfad statt Legacy-MCP |
| Video Frames Skill | Stills | OpenClaw/ClawHub; nur bei Bedarf |
| youtube-content Skill | Transkript→Text | Wenn Ausgabe Text, nicht Re-Encode |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Aufgabe klassifizieren: Datei-Op vs. Generativ vs. Text aus Video.
2. Tool-Policy prüfen: unnötige MCPs deaktivieren.
3. `ffprobe` auf Eingabedatei; Schnittprofil festlegen.
4. FFmpeg-Befehl ausführen oder Remotion-Render starten.
5. Ausgabe mit `ffprobe` und ggf. Framegrab verifizieren.
6. Kurzbericht: warum kein MCP / welches Skill genutzt.
7. Bei Katalog-Pfaden: Link zu remotion-dev/skills oder ffmpeg.org notieren.

## Qualitätskriterien / Definition of Done

- [ ] Geringstmögliche Tool-Menge aktiv
- [ ] Befehle reproduzierbar dokumentiert
- [ ] Kein MCP nur für `ffmpeg -version`
- [ ] Output technisch geprüft
- [ ] Freigaben bei Publish/Overwrite eingehalten

## Sicherheit & Freigaben

- MCP-Credentials nicht in argv; OAuth auf Connector-Backend (Grok-Bot-Wiki).
- Video mit personenbezogenen Daten: Verarbeitung nur lokal wenn möglich.

## Fallstricke

- MCP-Schema-Overhead kann Zehntausende Tokens kosten—vorher messen/policy.
- Fragmentierte FFmpeg-MCPs ohne klaren Maintainer—CLI bevorzugen.
- Skills vs. MCP verwechseln: Skills sind Procedures, keine Socket-Verbindung.
- Remotion ohne Skills → veraltete MCP-Namen in älteren Threads.
- Frame-Skill vs. ffmpeg: Doppelarbeit kostet Zeit und Kontext.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 30 s Teaser aus Webinar extrahieren.
- **Input:** `webinar.mkv`, 01:12:00 total, Ausschnitt ab 00:45:10.
- **Prompt:**

```text
Use ffmpeg only: cut 30s from 00:45:10, 1080p H.264 faststart. Explain why no video MCP.
```

- **Erwartetes Ergebnis:**

```bash
ffmpeg -ss 00:45:10 -i webinar.mkv -t 30 -vf scale=-2:1080 -c:v libx264 -crf 22 -c:a aac -movflags +faststart teaser.mp4
Rationale: single-pass transcode; MCP adds no capability.
```

### Beispiel 2 (Praxisbeispiel)

- **Aufgabe:** MCP-Token-Overhead bewusst vermeiden.
- **Input:** Policy erlaubt nur Terminal + ffmpeg.
- **Prompt:**

```text
Plan webinar cut but load zero video MCPs; cite r/ClaudeAI MCP overhead discussion if user asks about MCP.
```

- **Erwartetes Ergebnis:**

  Plan mit reinen Shell-Befehlen; Verweis https://www.reddit.com/r/ClaudeAI/comments/1ryz7zp/i_measured_my_mcp_token_overhead_67k_tokens/ ; kein MCP-Toolcall in der Ausführung.