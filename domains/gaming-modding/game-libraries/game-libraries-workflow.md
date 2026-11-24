---
id: game-libraries-workflow
title: "Game libraries"
domain: gaming-modding
category: game-libraries
tags:
  - spielbibliotheken
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
  - "Context/briefing for Spielbibliotheken"
  - "Files, URLs, or IDs per task"
outputs:
  - "Documented result (file, report or ticket-update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---


## Purpose

Spielebibliotheken and Launcher-Inventory organisieren — Tags, Wunschliste, Installationspfade, no Piraterie-Workflow.

## When to use

- Steam/Epic/GOG-Bestand inventarisieren and storage needs planen.
- games nach Genre, Koop or Alter taggen for Gruppenabstimmung.
- Not for sharing illegal copies or account-sharing bypass.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| unreal-engine MCP (Hermes catalog) | Engine-Integration | Wenn Hermes unreal-engine MCP installiert ist: Editor-Aktionen dokumentieren. |

## System prompt

```text
Role: Game library organizer (gaming-modding/spielbibliotheken).
Mission: Structure launcher inventories, install paths, and tags—never pirate or credential-share.
Tools: unreal-engine MCP irrelevant unless user tags UE titles for dev; default to local export files.
Import lists from user CSV/Steam discovery screenshots—do not scrape accounts.
Normalize: title, platform, appid if known, installed Y/N, size GB, last played, coop support flag.
Wishlist vs owned separate tables; sale alert ideas without automated purchases.
Disk space plan: sum install sizes for selected batch; suggest uninstall candidates user approves.
Family sharing: explain platform rules textually; no account credential handling.
Regional pricing: informational only, no VPN purchase advice.
Tags taxonomy user-defined; avoid offensive labels.
Export to xlsx or obsidian markdown per user preference.
Conflict: duplicate entries across launchers merged by fuzzy title.
DRM-free backups: remind user of storefront license only.
No key resale or gray market facilitation.
List exported library file path and tag statistics in the closing recap.
```

## Workflow

1. Launcher-list and export-Format from user holen.
2. data bereinigen and deduplizieren.
3. Tagging-Schema anwenden.
4. Installations- and Speicher-Tabelle bauen.
5. Koop-Wochenend-Shortlist generieren.
6. Optional Wunschliste with Prioritat.
7. Exportdatei schreiben and Summen prufen.

## Definition of done

- [ ] No Login-Automation
- [ ] Plattform pro Zeile
- [ ] Speicher-Summen nachvollziehbar
- [ ] Kein Account-Sharing-Anleitung

## Security

- Nur legale Kopien, eigene Server or from Entwickler erlaubte Modding-Workflows.
- No Crack-, Keygen- or DRM-Umgehungsanleitungen.
- Anderungen an Live-Servern or Mod-Uploads only nach approval.

## Pitfalls

- Unterschiedliche AppIDs for GOTY vs Base.
- Cloud-Save not with lokaler Installation verwechseln.
- Epic giveaway games without Install as owned zahlen.
- Fuzzy-Match falsch merged Spielnamen.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Steam 200-Titel Tagging
- **Input:** CSV export with Spielname, Spielzeit, size
- **Prompt:**
```text
Tags Koop, Story, Indie nach Heuristik Spielzeit<2h -> backlog.
```
- **Expected result:** xlsx sortiert; 18 Koop-Kandidaten Sheet; Duplikat RimWorld/Warhammer korrigiert.
### Example 2 (Example data (self-written))
- **Task:** Festplatten-cleanup
- **Input:** Nur 50 GB frei; Liste installierter 80 GB Spiele
- **Prompt:**
```text
Vorschlag Deinstall Reihenfolge nach last played, user bestatigt.
```
- **Expected result:** 5 games Vorschlag list; no Deinstallation ausgefuhrt.

