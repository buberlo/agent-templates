---
id: streaming-gaming-workflow
title: "Gaming-Streaming"
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
  - name: unreal-engine MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/unreal-engine"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Kontext/Briefing für Gaming-Streaming"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Streaming-Setup für Gaming: Szenen, Overlays, Audio-Routing und Clip-Workflows dokumentieren.

## Wann nutzen

- OBS/Streamlabs-Layout und Hotkeys für neues Setup planen.
- Overlay-Branding und Alert-Tests vorbereiten.
- Nicht für unbefugtes Restreaming urheberrechtlich geschützter Inhalte.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| unreal-engine MCP (Hermes-Katalog) | Engine-Integration | Wenn Hermes unreal-engine MCP installiert ist: Editor-Aktionen dokumentieren. |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Plattform, Auflösung, Hardware und Spiel festlegen.
2. Szenenliste und Quellenstruktur entwerfen.
3. Audio-Routing-Diagramm in Text.
4. Overlay-Dateipfade und Branding-Farben.
5. Hotkeys-Tabelle und Backup der scene collection.
6. Test-Stream-Checkliste.
7. Clip-Nachbearbeitungs-Workflow skizzieren.

## Qualitätskriterien / Definition of Done

- [ ] DMCA-Hinweis Musik
- [ ] Keine Copyright-Restreams
- [ ] OBS-Export beschrieben
- [ ] Test-Stream vor Public

## Sicherheit & Freigaben

- Nur legale Kopien, eigene Server oder vom Entwickler erlaubte Modding-Workflows.
- Keine Crack-, Keygen- oder DRM-Umgehungsanleitungen.
- Änderungen an Live-Servern oder Mod-Uploads nur nach Freigabe.
- Keine Veröffentlichung privater Chats in Overlays.

## Fallstricke

- Game Capture vs Display Capture falsche Wahl Vollbild.
- Mikrofon-Monitoring Feedback-Schleife.
- NVENC Treiber zu alt — in Checkliste.
- Alert-Volume ohne Limiter.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** OBS Szenen für Soulslike
- **Input:** 1080p60 NVENC, ein Monitor, Discord Voice
- **Prompt:**
```text
Szenen + Hotkeys F1–F4 und Audio-Bus Tabelle.
```
- **Erwartetes Ergebnis:** Markdown 6 Szenen; Discord-Quelle Separat; Test-Stream 6 Punkte.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Highlight Clips Workflow
- **Input:** Replay Buffer 120s, YouTube Highlights Upload
- **Prompt:**
```text
Namenskonvention und Export Schritte ohne automatischen Upload.
```
- **Erwartetes Ergebnis:** Ordnerstruktur clips/YYYY-MM-DD_title.md; Upload manuell Schrittfolge.

