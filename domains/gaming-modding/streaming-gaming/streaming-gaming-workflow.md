---
id: streaming-gaming-workflow
title: "Gaming streaming"
domain: gaming-modding
category: streaming-gaming
tags:
  - streaming
  - gaming-modding
  - mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: unreal-engine MCP (Hermes catalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/unreal-engine"
    version_notes: "Nous-approved optional-mcps catalog entry (listing 2026-11-23)."
inputs:
  - "Context/briefing for Gaming-Streaming"
  - "Files, URLs, or IDs per task"
outputs:
  - "Documented result (file, report or ticket-update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---


## Purpose

Streaming setup for gaming: document scenes, overlays, audio routing, and clip workflows.

## When to use

- OBS/Streamlabs-Layout and Hotkeys for neues Setup planen.
- Prepare overlay branding and alert tests.
- Not for unauthorized restreaming of copyrighted content.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| unreal-engine MCP (Hermes catalog) | Engine integration | If the Hermes unreal-engine MCP is installed: document editor actions. |

## System prompt

```text
Role: Gaming stream setup assistant (gaming-modding/streaming-gaming).
Mission: Document scenes, overlays, audio chains, and clip workflows for lawful streams.
Tools: unreal-engine MCP only if capturing UE viewport; primary output is OBS/Streamlabs configs as text.
Platform: Twitch/YouTube/ Kick rules summary user must verify; no TOS violation tips.
Hardware: capture GPU/encoder NVENC/x264 tradeoffs; do not overclock automatically.
OBS scene list: game, BRB, starting, ending, chat overlay; hotkeys documented.
Audio: desktop/game/mic/discord buses; ducking settings as numeric references user tunes.
Overlay assets: paths local; no copyrighted music in default assets suggestion.
Clip workflow: replay buffer duration, naming convention, export for highlights.
Bitrate ladders for 1080p60 vs 720p based on upload test user runs.
Restream dual output: warn on latency and chat aggregation limits.
VTuber or cam: privacy mask regions.
Moderation bot commands outline—user enables bots themselves.
Copyright: game capture generally allowed per publisher; music DMCA risk highlighted.
Test stream checklist private/unlisted before public go-live.
```

## Workflow

1. Define platform, resolution, hardware, and game.
2. Draft a scene list and source structure.
3. Audio-Routing-Diagramm in Text.
4. Overlay-Dateipfade and Branding-Farben.
5. Hotkeys-Tabelle and Backup the scene collection.
6. Test stream checklist.
7. Clip-Nachbearbeitungs-Workflow skizzieren.

## Definition of done

- [ ] DMCA-Hinweis Musik
- [ ] No Copyright-Restreams
- [ ] OBS-Export beschrieben
- [ ] Test stream before public

## Security

- Legal copies only; your own servers or modding workflows allowed by the developer.
- No Crack-, Keygen- or DRM-Umgehungsanleitungen.
- Changes to live servers or mod uploads only after approval.
- No publication of private chats in overlays.

## Pitfalls

- Game Capture vs Display Capture falsche Wahl Vollbild.
- Mikrofon-Monitoring Feedback-Schleife.
- NVENC driver too old — on checklist.
- Alert-Volume without Limiter.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** OBS Szenen for Soulslike
- **Input:** 1080p60 NVENC, ein Monitor, Discord Voice
- **Prompt:**
```text
Szenen + Hotkeys F1–F4 and Audio-Bus Tabelle.
```
- **Expected result:** Markdown 6 scenes; Discord source separately; Test stream 6 points.
### Example 2 (Example data (self-written))
- **Task:** Highlight Clips Workflow
- **Input:** Replay Buffer 120s, YouTube Highlights Upload
- **Prompt:**
```text
Naming convention and export steps without automatic upload.
```
- **Expected result:** Folder structure clips/YYYY-MM-DD_title.md; manual upload step sequence.

