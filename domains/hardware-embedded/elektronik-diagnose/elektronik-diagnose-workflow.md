---
id: elektronik-diagnose-workflow
title: "Elektronik-Diagnose"
domain: hardware-embedded
category: elektronik-diagnose
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
    install: "Shell des Agenten"
    version_notes: "Domain-Default laut Recherche"
inputs:
  - "Kontext/Briefing für Elektronik-Diagnose"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Schaltpläne lesen, Messwerte dokumentieren und Stücklisten für Fehlersuche strukturieren — keine Hochspannungsarbeit.

## Wann nutzen

- Board bring-up oder intermittierender Fehler mit Messprotokoll.
- Netzteil-Spannungen und Ripple loggen.
- Nicht für Netzspannung > SELV oder defekte LiPo-Feuerbekämpfung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Lokale Entwicklungsumgebung | Build & Flash | arduino-cli, idf.py, openocd, slicer-CLIs laut Projekt — nur mit freigegebenen Pfaden. |
| Versionskontrolle (Git) | Reproduzierbarkeit | Sketches, KiCad-Projekte und G-Code im Repo versionieren. |

## System-Prompt / Instruktionen

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

## Arbeitsablauf

1. Symptom, Schaltplan und letzte Änderungen sammeln.
2. BOM und kritische Nets identifizieren.
3. Messplan mit erwarteten Werten.
4. Nutzer trägt Messwerte ein oder dictiert.
5. Hypothesenliste priorisieren.
6. Sichere nächste Schritte (Komponente tauschen vs scope).
7. Abschlussprotokoll und Lessons learned.

## Qualitätskriterien / Definition of Done

- [ ] HV-Schritte ausgeschlossen oder STOP
- [ ] Messpunkte referenziert
- [ ] Hypothesen nicht als Fakten
- [ ] LiPo-Sicherheitsregel beachtet

## Sicherheit & Freigaben

- Keine Anleitungen für gefährliche Hochspannung oder defekte Netzteile ohne Fachperson.
- Flash/Bootloader nur mit Nutzerfreigabe und dokumentiertem Rollback.
- Seriennummern und Standortdaten in Logs minimieren.
- Bei Rauch, Hitze oder Schlag -> sofortiger Stopp; keine Weiteranalyse online.

## Fallstricke

- Multimeter auf Strom in Spannungsmessung.
- Ground clip auf falscher Masse Schleife.
- Ohne Entladevorgang Kondensator messen.
- Falscher IC Footprint einge lötet.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** 3.3V Rail fällt unter Last
- **Input:** KiCad PDF, LDO U2, erwartet 3.3 misst 3.0@200mA
- **Prompt:**
```text
Messplan 6 Punkte, Ripple mit Coupling Hinweis.
```
- **Erwartetes Ergebnis:** Tabelle Template; Hypothese undervoltage dropout; kein Löten empfohlen ohne Skill.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** I2C Bus sporadisch NACK
- **Input:** 100kHz, pullups 4k7, zwei slaves
- **Prompt:**
```text
Checkliste Adressenkonflikt, Länge, scope capture was Nutzer sehen soll.
```
- **Erwartetes Ergebnis:** 5 Debug-Schritte; Log-Spalten Zeit, Master, Addr, ACK.

