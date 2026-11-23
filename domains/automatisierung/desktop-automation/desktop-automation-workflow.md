---
id: desktop-automation-workflow
title: "Desktop-Automation"
domain: automatisierung
category: desktop-automation
tags:
  - desktop
  - automatisierung
  - skill
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: OS automation
    install: "xdotool / AppleScript / PowerShell UIA"
    version_notes: "Sichtbarer Desktop"
inputs:
  - "OS und Ziel-App"
outputs:
  - "Skript und Protokoll"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Desktop-Makros **sichtbar und protokolliert** — xdotool, osascript, pwsh — ohne Passwörter aus Chat.

## Wann nutzen

- Wiederkehrende GUI-Schritte am Arbeitsplatz.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| xdotool | Linux X11 | Fenster/Keys |
| osascript | macOS | AppleScript |

## System-Prompt / Instruktionen

```text
Role: desktop automation author (automatisierung/desktop-automation).
Mission: User-visible desktop only; delays 200-500ms; Wayland xdotool warning.
No passwords via synthesized keys.
Confirm before Alt+F4 Delete Format.
Handoff browser to browser-automation-workflow.
```

## Arbeitsablauf

1. OS und Apptitel erfassen.
2. Schritte bestätigen.
3. Skript mit Delays.
4. Dry-Run mit Nutzer.
5. Logging aktivieren.
6. Skript ablegen ohne Secrets.
7. Abbruch-Anleitung.

## Qualitätskriterien / Definition of Done

- [ ] Auf Ziel-OS getestet
- [ ] Keine Passwörter im Skript

## Sicherheit & Freigaben

- Nutzer muss zuschauen.

## Fallstricke

- Falsches Fenster fokussiert.
- Wayland + xdotool scheitert.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Writer PDF export
- **Input:** Ubuntu X11
- **Prompt:**

```text
xdotool activate Writer export pdf.
```

- **Erwartetes Ergebnis:**

```text
PDF exists user watched
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Wayland
- **Input:** Fedora
- **Prompt:**

```text
xdotool click form.
```

- **Erwartetes Ergebnis:**

```text
warn wayland limitation
```