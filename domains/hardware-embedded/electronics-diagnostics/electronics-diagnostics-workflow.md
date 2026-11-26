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

Read schematics, document measurements, and structure BOMs for troubleshooting — no high-voltage work.

## When to use

- Board bring-up or intermittierender Fehler with Messprotokoll.
- Log power supply voltages and ripple.
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

1. Collect symptoms, schematic, and recent changes.
2. BOM and kritische Nets identifizieren.
3. Messplan with erwarteten Werten.
4. User enters or dictates measurements.
5. Prioritize hypothesis list.
6. Safe next steps (swap component vs. scope).
7. Abschlussprotokoll and Lessons learned.

## Definition of done

- [ ] HV steps excluded or STOP
- [ ] Messpunkte referenziert
- [ ] Hypotheses not presented as facts
- [ ] LiPo-Sicherheitsregel beachtet

## Security

- No Anleitungen for gefahrliche high voltage or defekte power supplies without qualified person.
- Flash/bootloader only with user approval and documented rollback.
- Seriennummern and Standortdaten in Logs minimieren.
- In case of smoke, heat, or shock -> immediate stop; no further online analysis.

## Pitfalls

- Multimeter on Strom in Spannungsmessung.
- Ground clip on wrong ground loop.
- Measuring capacitor without discharging first.
- Wrong IC footprint soldered in.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** 3.3V rail drops under load
- **Input:** KiCad PDF, LDO U2, erwartet 3.3 misst 3.0@200mA
- **Prompt:**
```text
Messplan 6 Punkte, Ripple with Coupling Hinweis.
```
- **Expected result:** Tabelle Template; Hypothese undervoltage dropout; no Loten empfohlen without Skill.
### Example 2 (Example data (self-written))
- **Task:** I2C Bus sporadisch NACK
- **Input:** 100kHz, pullups 4k7, zwei slaves
- **Prompt:**
```text
Checklist for address conflict, length, and scope capture of what the user should see.
```
- **Expected result:** 5 debug steps; log columns Time, Master, Addr, ACK.

