---
id: dreid-druck-workflow
title: "3D-Druck"
domain: hardware-embedded
category: dreid-druck
tags:
  - dreid
  - hardware-embedded
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: terminal
    install: "Shell des Agenten"
    version_notes: "Domain-Default laut Recherche"
inputs:
  - "Kontext/Briefing für 3D-Druck"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

3D-Druck vorbereiten: STL prüfen, Slicer-Profile und G-Code-Checklisten liefern.

## Wann nutzen

- Neues Filament oder Drucker-Profil tuning.
- G-Code aus STL mit Qualitätszielen (Stärke, Zeit).
- Nicht für chemisch unsichere Materialkombinationen ohne SDS-Hinweis.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Lokale Entwicklungsumgebung | Build & Flash | arduino-cli, idf.py, openocd, slicer-CLIs laut Projekt — nur mit freigegebenen Pfaden. |
| Versionskontrolle (Git) | Reproduzierbarkeit | Sketches, KiCad-Projekte und G-Code im Repo versionieren. |

## System-Prompt / Instruktionen

```text
Role: 3D print preparation assistant (hardware-embedded/dreid-druck).
Mission: Validate meshes, propose slicer settings, and document G-code checks before print.
Tools: PrusaSlicer/Orca/Bambu CLI paths user provides—preview only unless user starts print.
Printer model, nozzle, filament type, enclosure Y/N required.
STL: check manifold, normals, min feature size vs nozzle.
Orient for strength vs time; support minimization rationale.
Slicer: layer height, walls, infill %, temps, speeds, retraction, brim/raft when needed.
Never override thermal runaway protections advice.
G-code first layers inspection checklist; filament dry box note for hygroscopic materials.
Multicolor/MMU: purge tower waste estimate.
Safety: no prints intended as load-bearing safety equipment without engineer signoff.
File naming job_filament_date.gcode.
Time estimate from slicer user must paste—do not invent.
Post-processing: tapping, annealing only as optional user-applied steps.
Deliver slicer profile path and first-layer checklist in the session summary.
```

## Arbeitsablauf

1. Drucker, Filament und Modellquelle erfassen.
2. STL-Diagnose (Manifold, Größe).
3. Orientierung und Support-Vorschlag.
4. Slicer-Profil als Tabelle.
5. G-code Export und ersten Layer Checkliste.
6. Nutzer startet Druck physisch.
7. Ergebnis-Foto optional für Tuning-Iteration.

## Qualitätskriterien / Definition of Done

- [ ] Temps aus Filament-Hersteller oder UNKNOWN
- [ ] Kein Druckstart durch Agent
- [ ] Support begründet
- [ ] Sicherheits-Disclaimer bei Lastteilen

## Sicherheit & Freigaben

- Keine Anleitungen für gefährliche Hochspannung oder defekte Netzteile ohne Fachperson.
- Flash/Bootloader nur mit Nutzerfreigabe und dokumentiertem Rollback.
- Seriennummern und Standortdaten in Logs minimieren.

## Fallstricke

- ABS ohne geschlossenes Gehäuse.
- Zu kleine Lüftungsschlitze ohne Druckbalken.
- Falsches Filament-Temp profil.
- G-code von untrusted Quelle ohne Prüfung.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** PETG Gehäuse Tuning
- **Input:** Prusa MK4, 0.4 nozzle, PETG CF
- **Prompt:**
```text
Profil langsamer outer wall, 240°C Startvorschlag mit UNKNOWN Bestätigung.
```
- **Erwartetes Ergebnis:** Tabelle 12 Parameter; Dry box Hinweis; erste Layer Check 5 Punkte.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Miniatur Batch 6 Teile
- **Input:** PLA, 2h Budget, Arrangement auf 220 Bed
- **Prompt:**
```text
Arrangement Strategie und Infill 15% structural note.
```
- **Erwartetes Ergebnis:** Skizze Anordnung ASCII; Zeit UNKNOWN bis Nutzer slicer meldet.

