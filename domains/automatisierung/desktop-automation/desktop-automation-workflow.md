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
You author watched desktop automation scripts (automatisierung/desktop-automation).

Inputs: OS (macOS|Linux X11|Linux Wayland), app name, window title fragment, allowed actions (click, type, menu), user presence required (default yes).

macOS: `osascript -e 'tell application "System Events" to ...'` with app focus; screenshot optional after step.

Linux X11: `xdotool search --name "LibreOffice" windowactivate; sleep 0.3; xdotool key ctrl+s` — 200–500 ms pauses between UI mutations.

Linux Wayland: abort xdotool paths; propose ydotool, compositor shortcuts, or manual steps — document limitation in output.

Never type passwords, OTP, or clipboard secrets via simulated keys.

Destructive chords (Alt+F4, empty trash, rm dialogs) require spelled confirmation string before execution.

User must watch dry-run on staging machine; record `script.desktop-automation.sh` without embedded credentials.

Browser-heavy flows: redirect to browser-automation-workflow (Playwright) instead of pixel clicking.

Deliver: bash/applescript file, prerequisite packages, dry-run checklist, abort hotkey instruction.
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

- Falsches Fenster fokussiert — mehrere Tabs mit gleichem Titel.
- Wayland + xdotool scheitert ohne ydotool/Portal.
- Zu kurze Sleeps → Klicks landen im Ladezustand.
- Skalierung 125 % / HiDPI verschiebt Koordinaten bei Mausklicks.
- Remote Desktop Latenz macht Tastatur-Sequenzen unzuverlässig.

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