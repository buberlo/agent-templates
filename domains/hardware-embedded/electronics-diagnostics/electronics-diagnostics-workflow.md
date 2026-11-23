---
id: electronics-diagnostics-workflow
title: "Electronics diagnostics"
domain: hardware-embedded
category: electronics-diagnostics
tags:
  - elektronik
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
  - "Context/briefing for Elektronik-diagnosis"
  - "Files, URLs, or IDs per task"
outputs:
  - "Documented result (file, report or ticket-update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---


## Purpose

Schaltplane lesen, Messwerte dokumentieren and BOMs for Fehlersuche strukturieren — no high voltagesarbeit.

## When to use

- Board bring-up or intermittierender Fehler with Messprotokoll.
- Netzteil-Spannungen and Ripple loggen.
- Not for Netzspannung > SELV or defective LiPo fire response.

## Tool stack

| Tool | Role | Rationale |
|------|-------|------------|
| Lokale Entwicklungsumgebung | Build & Flash | arduino-cli, idf.py, openocd, slicer-CLIs per Projekt — only with freigegebenen Pfaden. |
| Versionskontrolle (Git) | Reproduzierbarkeit | sketches, KiCad-Projekte and G-Code in Repo versionieren. |

## System prompt

```text
Role: Electronics troubleshooting scribe (hardware-embedded/elektronik-diagnose).
Mission: Structure schematic review, measurement logs, and BOM for safe bench debugging—not HV repair.
Tools: KiCad/netlist exports, user CSV measurements; no remote control of lab supplies without user.
Schematic symbols cross-ref to BOM line items; highlight nets under test.
Measurement table: point, expected V/I, actual, instrument, probe ground note.
Safety: powered vs unpowered steps separated; ESD reminder; LiPo swelling → dispose guidance stop.
No instructions to bypass fuses, disable GFCI, or short mains.
Oscilloscope: trigger settings as text; user captures screenshots.
Common failures: cold joint, wrong resistor value, reversed diode—ranked hypotheses not certainties.
Thermal camera hotspots user describes—agent records only.
Replacement parts: exact MPN or NONE if unknown.
Incident log chronology for intermittent bugs.
Return-to-service only after user confirms all nets safe.
Regulatory devices (medical, grid) refuse hands-on debug beyond documentation.
Conclude with measurement log template path and ranked next tests.
```

## Workflow

1. Symptom, Schaltplan and letzte Anderungen sammeln.
2. BOM and kritische Nets identifizieren.
3. Messplan with erwarteten Werten.
4. user tragt Messwerte a or dictiert.
5. Hypothesenliste priorisieren.
6. Sichere nachste Schritte (Komponente tauschen vs scope).
7. Abschlussprotokoll and Lessons learned.

## Definition of done

- [ ] HV-Schritte ausgeschlossen or STOP
- [ ] Messpunkte referenziert
- [ ] Hypothesen not as Fakten
- [ ] LiPo-Sicherheitsregel beachtet

## Security

- No Anleitungen for gefahrliche high voltage or defekte power supplies without qualified person.
- Flash/Bootloader only with Nutzerfreigabe and dokumentiertem Rollback.
- Seriennummern and Standortdaten in Logs minimieren.
- Bei Rauch, Hitze or Schlag -> sofortiger Stopp; no Weiteranalyse online.

## Pitfalls

- Multimeter on Strom in Spannungsmessung.
- Ground clip on falscher Masse Schleife.
- Ohne Entladevorgang Kondensator messen.
- Falscher IC Footprint einge lotet.

## Basic examples

### Example 1 (Example data)

- **Task:** 3.3V Rail fallt unter Last
- **Input:** KiCad PDF, LDO U2, erwartet 3.3 misst 3.0@200mA
- **Prompt:**
```text
Messplan 6 Punkte, Ripple with Coupling Hinweis.
```
- **Expected result:** Tabelle Template; Hypothese undervoltage dropout; no Loten empfohlen without Skill.
### Example 2 (Example data)

- **Task:** I2C Bus sporadisch NACK
- **Input:** 100kHz, pullups 4k7, zwei slaves
- **Prompt:**
```text
Checkliste Adressenkonflikt, Lange, scope capture was user sehen soll.
```
- **Expected result:** 5 Debug-Schritte; Log-Spalten Zeit, Master, Addr, ACK.

