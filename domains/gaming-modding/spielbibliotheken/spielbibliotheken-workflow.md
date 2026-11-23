---
id: spielbibliotheken-workflow
title: "Spielbibliotheken"
domain: gaming-modding
category: spielbibliotheken
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
  - name: unreal-engine MCP (Hermes-Katalog)
    install: "https://github.com/NousResearch/hermes-agent/tree/main/optional-mcps/unreal-engine"
    version_notes: "Nous-approved optional-mcps-Katalogeintrag (Listing 23.11.2026)."
inputs:
  - "Kontext/Briefing für Spielbibliotheken"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Spielebibliotheken und Launcher-Inventar organisieren — Tags, Wunschliste, Installationspfade, kein Piraterie-Workflow.

## Wann nutzen

- Steam/Epic/GOG-Bestand inventarisieren und Speicherbedarf planen.
- Spiele nach Genre, Koop oder Alter taggen für Gruppenabstimmung.
- Nicht zum Teilen illegaler Kopien oder Account-Sharing-Bypass.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| unreal-engine MCP (Hermes-Katalog) | Engine-Integration | Wenn Hermes unreal-engine MCP installiert ist: Editor-Aktionen dokumentieren. |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Launcher-Liste und Export-Format vom Nutzer holen.
2. Daten bereinigen und deduplizieren.
3. Tagging-Schema anwenden.
4. Installations- und Speicher-Tabelle bauen.
5. Koop-Wochenend-Shortlist generieren.
6. Optional Wunschliste mit Priorität.
7. Exportdatei schreiben und Summen prüfen.

## Qualitätskriterien / Definition of Done

- [ ] Keine Login-Automation
- [ ] Plattform pro Zeile
- [ ] Speicher-Summen nachvollziehbar
- [ ] Kein Account-Sharing-Anleitung

## Sicherheit & Freigaben

- Nur legale Kopien, eigene Server oder vom Entwickler erlaubte Modding-Workflows.
- Keine Crack-, Keygen- oder DRM-Umgehungsanleitungen.
- Änderungen an Live-Servern oder Mod-Uploads nur nach Freigabe.

## Fallstricke

- Unterschiedliche AppIDs für GOTY vs Base.
- Cloud-Save nicht mit lokaler Installation verwechseln.
- Epic giveaway Spiele ohne Install als owned zählen.
- Fuzzy-Match falsch merged Spielnamen.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Steam 200-Titel Tagging
- **Input:** CSV export mit Spielname, Spielzeit, Größe
- **Prompt:**
```text
Tags Koop, Story, Indie nach Heuristik Spielzeit<2h -> backlog.
```
- **Erwartetes Ergebnis:** xlsx sortiert; 18 Koop-Kandidaten Sheet; Duplikat RimWorld/Warhammer korrigiert.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Festplatten-Räumung
- **Input:** Nur 50 GB frei; Liste installierter 80 GB Spiele
- **Prompt:**
```text
Vorschlag Deinstall Reihenfolge nach last played, Nutzer bestätigt.
```
- **Erwartetes Ergebnis:** 5 Spiele Vorschlag Liste; keine Deinstallation ausgeführt.

