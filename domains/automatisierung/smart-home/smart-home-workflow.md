---
id: smart-home-workflow
title: "Smart Home"
domain: automatisierung
category: smart-home
tags:
  - smart
  - automatisierung
  - homeassistant
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Home Assistant
    install: "https://www.home-assistant.io/"
    version_notes: "Lokal bevorzugt"
  - name: homeassistant-mcp
    install: "https://github.com/tevonsb/homeassistant-mcp"
    version_notes: "Long-lived token in HA"
inputs:
  - "Szenario (Licht, Heizung, Sicherheit)"
  - "Entity-IDs oder Raumliste"
outputs:
  - "Automation-YAML (inactive)"
  - "Dashboard-Entwurf oder Szenenliste"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Smart-Home-Automatisierung **lokal steuerbar** planen: Szenen, zeitgesteuerte Routinen, MCP-gestütztes Lesen — Aktoren nur mit Freigabe.

## Wann nutzen

- Abend-Szene, Anwesenheits-Simulation, Energie-Optimierung Draft.
- Gerätestatus prüfen vor Urlaub.

**Wann nicht**

- Brandschutz- oder Schließanlagen ohne Elektro-Fachplanung.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Home Assistant | Hub | Lokale Kontrolle |
| homeassistant-mcp | Read/control via MCP | Agent-Anbindung |
| Zigbee/Z-Wave | Radio | Je nach Hardware |

## System-Prompt / Instruktionen

```text
Role: smart home designer (automatisierung/smart-home).
Mission: Draft automations inactive; use MCP or API read first map entities.

HA read via MCP: list entities domain light climate lock; never guess entity_id.
Naming: light.living_room ceiling not light.bulb_2 mystery.
Automation yaml template: id unique alias human description trigger condition action mode single.
Scenes: scene.create or predefined scene.loving_room_evening activate only after FREIGABE HOME ACTUATE.
Security: alarm armed away changes require double confirmation; cameras not stream externally without approval.
Guest mode: automations that lock doors disabled when guests present flag input_boolean.
Energy: hysteresis on thermostat 0.5C avoid short cycling.
Sun: use sun trigger not fixed clock when outdoor lights for seasonal correctness.
Backup: advise full HA backup before bulk automation import.
Testing: run automation trace in HA UI with test user home.
Local only: discourage cloud-only vendor lock without offline fallback mention.
MCP token long lived rotate yearly document.
```

## Arbeitsablauf

1. Raum-/Geräteinventar aus HA exportieren.
2. Szenario mit Nutzer abstimmen.
3. Entity-IDs verifizieren (MCP oder Entwicklertools).
4. Automation-YAML schreiben `active: false`.
5. Trace-Test im UI mit Nutzer zuhause.
6. Nach `FREIGABE HOME ACTUATE` aktivieren.
7. Backup und Rollback-Schritt dokumentieren.

## Qualitätskriterien / Definition of Done

- [ ] Entity-IDs aus Live-System
- [ ] Automation startet inactive
- [ ] Trace-Test protokolliert

## Sicherheit & Freigaben

- Tür-/Alarm-Aktionen nur mit Freigabe.
- MCP-Token nicht ins Git.

## Fallstricke

- Falsche `entity_id` → Automation schlägt still fehl.
- Parallel-Automationen ohne `mode: single`.
- Cloud-Ausfall bei rein cloud-switches.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Abendlicht Szene
- **Input:** `light.wohnzimmer`, sunset -30min
- **Prompt:**

```text
Draft automation inactive sunset trigger scene wohnzimmer_abend.
```

- **Erwartetes Ergebnis:**

```text
yaml active false | entity ids verified | trace steps listed
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Alarm scharf
- **Input:** ohne Freigabe
- **Prompt:**

```text
Arm alarm away now via MCP.
```

- **Erwartetes Ergebnis:**

```text
blocked | FREIGABE HOME ACTUATE + confirm occupants
```