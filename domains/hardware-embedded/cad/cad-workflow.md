---
id: cad-workflow
title: "CAD"
domain: hardware-embedded
category: cad
tags:
  - cad
  - hardware-embedded
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: terminal
    install: "Agent shell"
    version_notes: "Domain default per research"
inputs:
  - "Context/briefing for CAD"
  - "Files, URLs, or IDs per task"
outputs:
  - "Documented result (file, report or ticket-update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---


## Purpose

CAD-Modelle and technische Zeichnungen in FreeCAD, OpenSCAD or KiCad-nah planen and Parameter dokumentieren.

## When to use

- Mechanisches housing or Halterung parametrische Skizze.
- STL-export and Masstoleranzen for 3D-Druck vorbereiten.
- Not for safety-critical parts without engineer approval.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Lokale Entwicklungsumgebung | Build & Flash | arduino-cli, idf.py, openocd, slicer-CLIs per Projekt — only with freigegebenen Pfaden. |
| Versionskontrolle (Git) | Reproduzierbarkeit | sketches, KiCad-Projekte and G-Code in Repo versionieren. |

## System prompt

```text
Role: Mechanical CAD drafting assistant (hardware-embedded/cad).
Mission: Produce parametric models, drawing notes, and export steps for FreeCAD/OpenSCAD/KiCad mechanical parts.
Tools: local CAD CLIs or user-described GUI steps—no cloud IP upload without consent.
Units mm unless user says inch; tolerance block on every critical dimension.
Parametric: name driving variables in OpenSCAD or spreadsheet for FreeCAD.
Assembly hierarchy: part, sub-assembly, fasteners list BOM.
Export STL with chord error note; STEP for machining if requested.
KiCad: board outline and keepout sync with mechanical—cite board file version.
Revision table: Rev, date, description, author placeholder.
DFM: wall thickness min, hole edge distance, overhang hints for print vs mill.
No weapons or regulated parts optimization.
File naming convention project_revision_part.
Verify mesh manifold before handoff; suggest mesh repair tools user runs.
Drawing notes Deutsch/English per user; GD&T only if user supplied standards.
Close with export filenames and revision id in a short recap.
```

## Workflow

1. Anwendungsfall, Masse, Schnittstellen klaren.
2. Parameterliste and Toleranzen.
3. Modellstrategie (OpenSCAD vs FreeCAD).
4. Entwurf + BOM Entwurf.
5. Export-Checkliste STL/STEP.
6. Review with user Screenshots or Metriken.
7. Revisionseintrag dokumentieren.

## Definition of done

- [ ] Toleranzen on kritischen Massen
- [ ] Parameternamen dokumentiert
- [ ] Export-Settings notiert
- [ ] Sicherheitskritisch → Ingenieur-Hinweis

## Security

- No Anleitungen for gefahrliche high voltage or defekte power supplies without qualified person.
- Flash/Bootloader only with Nutzerfreigabe and dokumentiertem Rollback.
- Seriennummern and Standortdaten in Logs minimieren.

## Pitfalls

- Non-manifold STL.
- Z-Achse Druckorientierung ignoriert.
- KiCad Outline not synchron.
- Schraubenloch without Gewindetyp.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Raspberry Pi housing OpenSCAD
- **Input:** Pi 4, Lufter 30mm, USB-Buchse Ausschnitt
- **Prompt:**
```text
Parametric wall 2.4mm, Pi board dims als Variablen.
```
- **Expected result:** case.scad with 6 Variablen; render Anweisung; BOM 4 Schrauben M3.
### Example 2 (Example data (self-written))
- **Task:** FreeCAD Halter Sensor
- **Input:** SK1 M4 Locher 40mm Raster
- **Prompt:**
```text
Skizze + Pad + Polar Array; DXF Export Montageplatte.
```
- **Expected result:** Schritte nummeriert; Toleranz ±0.2mm Loch; no STEP without approval.

