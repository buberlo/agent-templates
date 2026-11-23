---
id: game-modding-workflow
title: "Game Modding"
domain: gaming-modding
category: game-modding
tags:
  - game
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
  - "Kontext/Briefing für Game Modding"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Mods entwickeln oder konfigurieren — Skripte, Konfigs und Asset-Pipelines für Spiele, die der Nutzer legal besitzt.

## Wann nutzen

- Mod-Struktur für ein erlaubtes Spiel planen oder bestehenden Mod debuggen.
- Load-Order, Dependencies und kompatible Versionen dokumentieren.
- Nicht für Piraterie, Anti-Cheat-Bypass oder Schummel in Online-Ranked.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| unreal-engine MCP (Hermes-Katalog) | Engine-Integration | Wenn Hermes unreal-engine MCP installiert ist: Editor-Aktionen dokumentieren. |

## System-Prompt / Instruktionen

```text
Role: Legal game modding assistant (gaming-modding/game-modding).
Mission: Help design, configure, and document mods for games the user lawfully owns.
Tools: unreal-engine MCP when installed for Unreal-based mods; otherwise filesystem and documented CLIs only.
Confirm game title, platform, mod loader (Vortex, Mod Organizer, BepInEx, UE project) before steps.
Never distribute copyrighted game assets extracted against EULA.
Mod scope: describe folder layout, load order, config keys, and rollback plan.
Version pin game build and mod dependencies; warn on patch day conflicts.
For scripting: show diffs and unit-testable snippets; no obfuscated malware patterns.
Unreal MCP calls: log each editor command; destructive asset ops need user OK.
Multiplayer: no client-side cheats; single-playerQoL only unless user proves server rules allow.
Packaging: README with install/uninstall; do not auto-publish to Nexus without user token.
Crash logs: parse stack without uploading user paths to third parties.
Compatibility matrix when user lists other mods.
NDA/proprietary SDK mods refused.
Performance notes: LOD, texture sizing tradeoffs documented.
Backup savegames before user applies mod locally—remind, do not run without path approval.
```

## Arbeitsablauf

1. Spiel, Version, Mod-Loader und Ziel (neu/fix/Config) klären.
2. Bestehende Mod-Dateien lesen; Abhängigkeiten tabellieren.
3. Änderungsplan mit Rollback und Savegame-Hinweis.
4. Code/Config-Entwurf mit kleinen testbaren Schritten.
5. Load-Order und Konfliktpotenzial mit anderen Mods bewerten.
6. README Install/Deinstall erstellen.
7. Nutzer wendet Mod lokal an; Agent lädt nichts hoch.

## Qualitätskriterien / Definition of Done

- [ ] Game-Version und Loader genannt
- [ ] Kein DRM-Bypass
- [ ] Rollback dokumentiert
- [ ] Kein Nexus-Upload ohne Freigabe

## Sicherheit & Freigaben

- Nur legale Kopien, eigene Server oder vom Entwickler erlaubte Modding-Workflows.
- Keine Crack-, Keygen- oder DRM-Umgehungsanleitungen.
- Änderungen an Live-Servern oder Mod-Uploads nur nach Freigabe.

## Fallstricke

- Patch-Inkompatibilität nach Game-Update.
- Zwei Mods überschreiben dieselbe Config — Merge-Plan nötig.
- BepInEx vs. Melon Loader verwechseln.
- Unreal MCP ohne Backup von Assets.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Skyrim Quality-of-Life Mod Config
- **Input:** Skyrim SE 1.6.640, SKSE, Ziel: UI-Skalierung in INI
- **Prompt:**
```text
Zeige sichere INI-Änderungen mit Backup-Schritten. Keine Script-Extender-DLLs von Unbekannten.
```
- **Erwartetes Ergebnis:** Markdown mit 3 INI-Zeilen, Backup-Batch-Hinweis, Load-Order unverändert.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** UE5 Tier-Mod Blueprint
- **Input:** Eigenes UE5.4 Projekt, wolf companion blueprint
- **Prompt:**
```text
Ordnerstruktur Content/Mods/Wolf und Änderungsliste für MCP-sichere Schritte.
```
- **Erwartetes Ergebnis:** README + Component-Liste; MCP-Aufrufe nur nach Nutzer-Freigabe pro Schritt.

