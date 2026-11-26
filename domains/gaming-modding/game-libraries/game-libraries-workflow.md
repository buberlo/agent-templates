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
- Tag games by genre, co-op, or age for group voting.
- Not for sharing illegal copies or account-sharing bypass.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| unreal-engine MCP (Hermes catalog) | Engine integration | If the Hermes unreal-engine MCP is installed: document editor actions. |

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
7. Write export file and verify totals.

## Definition of done

- [ ] No Login-Automation
- [ ] Plattform pro Zeile
- [ ] Speicher-Summen nachvollziehbar
- [ ] No account-sharing instructions

## Security

- Legal copies only; your own servers or modding workflows allowed by the developer.
- No Crack-, Keygen- or DRM-Umgehungsanleitungen.
- Changes to live servers or mod uploads only after approval.

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
Tags co-op, story, indie by heuristic playtime<2h -> backlog.
```
- **Expected result:** xlsx sortiert; 18 Koop-Kandidaten Sheet; Duplikat RimWorld/Warhammer korrigiert.
### Example 2 (Example data (self-written))
- **Task:** Festplatten-cleanup
- **Input:** Only 50 GB free; list of installed 80 GB games
- **Prompt:**
```text
Suggested uninstall order by last played, user confirms.
```
- **Expected result:** 5 games Vorschlag list; no Deinstallation ausgefuhrt.

