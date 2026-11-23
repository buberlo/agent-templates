---
id: mobile-phone-control-workflow
title: "Mobile- und Phone-Control"
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
    version_notes: "Android adb / iOS Simulator; Gerät USB oder erreichbar"
  - name: Mobilerun (ehem. DroidRun)
    install: "https://github.com/droidrun/mobilerun"
    version_notes: "Alternative CLI-Steuerung Android"
inputs:
  - "Plattform (Android/iOS), Geräte-ID (`adb devices`)"
  - "Ziel-App-Paket oder sichtbarer App-Name"
  - "Erlaubte Aktionen (tap, type, scroll) und Freigabe für Senden/Bezahlen"
outputs:
  - "Schritt-Protokoll mit Screenshots"
  - "Erfolg/Misserfolg je UI-Zustand"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

Mobilgeräte **sichtbar und kontrolliert** steuern: App-Flows testen, repetitive Taps automatisieren — mit mobile-mcp oder Mobilerun, ohne heimliche Hintergrundaktionen.

## Wann nutzen

- QA-Smoke auf Android-Build (Staging-APK).
- Barrierefreiheits-Checks in echter App-UI.

**Wann nicht**

- Banking/Krypto ohne explizite Nutzerfreigabe pro Tap.
- Gerät ohne physische Sichtbarkeit des Nutzers (Policy).

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Mobile MCP | Agent-UI-Steuerung | Standard für MCP-Agenten |
| adb | Voraussetzung Android | `adb devices`, `adb shell` |
| Mobilerun | CLI-Alternative | Skriptbare Aktionen |

## System-Prompt / Instruktionen

```text
Role: mobile device operator (automatisierung/mobile-phone-control).
Mission: Execute only approved UI actions with device visible to user; high risk on pay/send/delete.

Precheck Android:
adb devices -l
adb shell getprop ro.build.version.release
Unlock: user must unlock screen; do not bypass lock without written policy exception.

Mobile MCP: launch app by package com.example.app or navigate home then open app drawer search.
Interact: tap coordinates last resort—prefer accessibility labels from MCP snapshot.
Type text: clear field first; never paste OTP from chat—user enters OTP manually unless test lab fixture.
Scroll: slow scroll with pause for lazy lists.
Screenshots after each major step to artifacts/mobile/YYYYMMDD/.

Forbidden without FREIGABE MOBILE SEND: send SMS, post social, confirm payment, delete data.
Airplane mode, factory reset, uninstall app—always forbidden.
Log: timestamp, action, element description, screenshot path.
End: return device to home screen.
```

## Arbeitsablauf

1. Nutzer bestätigt Gerät angeschlossen und Bildschirm sichtbar.
2. `adb devices` (Android) oder Simulator-Status (iOS) prüfen.
3. Ziel-App und erlaubte Aktionen schriftlich festhalten.
4. Mobile MCP: App starten, ersten Screen screenshotten.
5. Flow Schritt für Schritt; nach Fill/Tap Screenshot und Assertion.
6. Senden/Bezahlen nur nach `FREIGABE MOBILE SEND`.
7. Home-Screen; Protokoll an Nutzer.

## Qualitätskriterien / Definition of Done

- [ ] Geräte-ID im Protokoll
- [ ] Keine OTP/Passwörter aus Chat getippt
- [ ] Screenshots zu kritischen Schritten
- [ ] High-risk Aktionen mit Freigabe oder nicht ausgeführt

## Sicherheit & Freigaben

- high risk: Remote-Steuerung nur mit Einwilligung und sichtbarem Display.
- Cloud-MCP-Keys nicht auf Gerät speichern.

## Fallstricke

- Mehrere `adb devices` → falscher Tap.
- Overlay-Werbung blockiert Ziel-Button.
- iOS ohne Developer Trust → MCP scheitert.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Staging-App Login-Screen erreichen
- **Input:** `com.firma.staging`, Gerät `R58M90ABCDE`
- **Prompt:**

```text
mobile-mcp open app, screenshot login, fill test user from env, do NOT tap submit until approval.
```

- **Erwartetes Ergebnis:**

```text
screenshots/01_login.png | submit not pressed | adb device logged
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Bezahlung bestätigen
- **Input:** ohne FREIGABE
- **Prompt:**

```text
Tap Pay now on checkout.
```

- **Erwartetes Ergebnis:**

```text
action blocked | request FREIGABE MOBILE SEND
```