---
id: mobile-phone-control-mcp-focus
title: "Mobile- und Phone-Control: MCP/Skill-Fokus"
domain: automatisierung
category: mobile-phone-control
tags:
  - mobile
  - automatisierung
  - mobile-mcp
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: Mobile MCP
    install: "https://github.com/mobile-next/mobile-mcp"
    version_notes: "stdio MCP; adb prerequisites"
  - name: Mobilerun (ehem. DroidRun)
    install: "https://github.com/droidrun/mobilerun"
    version_notes: "CLI parallel nur wenn Nutzer will"
inputs:
  - "Client-Plattform und aktive MCP-Liste"
  - "Android vs iOS vs Companion-App"
outputs:
  - "Empfohlene MCP/Companion-Kombination"
  - "Precheck-Kommandos (adb, Simulator)"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

**mobile-mcp vs. Mobilerun vs. Companion** routen: minimales Setup, adb-Voraussetzungen, Policy für High-Risk-Aktionen vor der ersten Tap.

## Wann nutzen

- Vor einer Mobile-Automation-Session Tool-Landschaft klären.
- Fehler „kein Gerät gefunden“ → Precheckliste.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Mobile MCP | UI automation | MCP-native Agenten |
| Mobilerun | CLI | Skriptbare Android-Flows |
| OpenClaw Companion | Relay | Nicht Agent-Host |

## System-Prompt / Instruktionen

```text
Role: mobile MCP advisor (automatisierung/mobile-phone-control-mcp-focus).
Mission: Select one primary control plane; document adb/simulator prerequisites.

Android path: platform-tools; USB debugging; adb devices authorized.
Mobile MCP config: add server mobile-mcp; prefer accessibility tree taps.
Mobilerun: when user wants shell scripts without full MCP snapshot cost.
Do not run Mobilerun and Mobile MCP competing taps same session.
High risk: FREIGABE MOBILE SEND token in parent workflow.
Precheck: adb version; adb devices -l; package grep fragment.
Handoff to mobile-phone-control-workflow after tool choice frozen.
```

## Arbeitsablauf

1. Plattform und Gerätetyp erfragen.
2. Precheck-Kommandos ausgeben.
3. Mobile MCP vs Mobilerun entscheiden.
4. include-Liste vorschlagen.
5. High-Risk-Policy nennen.
6. Verweis auf Workflow-Template.

## Qualitätskriterien / Definition of Done

- [ ] Genau ein primäres Steuerungs-Tool empfohlen
- [ ] adb Precheck dokumentiert
- [ ] FREIGABE MOBILE SEND erwähnt

## Sicherheit & Freigaben

- Companion-App ≠ Speicher für API-Keys.

## Fallstricke

- Zwei Steuerungen parallel → Ghost-taps.
- MCP ohne adb auf PATH → sofortiger Fehler.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Toolwahl Android QA
- **Input:** Hermes, USB-Gerät
- **Prompt:**

```text
Which MCP for tap-through staging app?
```

- **Erwartetes Ergebnis:**

```text
mobile-mcp primary | adb devices checklist
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** iOS ohne Mac
- **Input:** Windows host
- **Prompt:**

```text
Automate iOS app on real iPhone.
```

- **Erwartetes Ergebnis:**

```text
block or cloud farm | no false promise local iOS
```