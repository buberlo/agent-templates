---
id: arduino-esp32-workflow
title: "Arduino und ESP32"
domain: hardware-embedded
category: arduino-esp32
tags:
  - arduino
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
  - "Kontext/Briefing für Arduino und ESP32"
  - "Dateien, URLs oder IDs laut Aufgabe"
outputs:
  - "Dokumentiertes Ergebnis (Datei, Bericht oder Ticket-Update)"
risk_level: low
example_count: 2
version: "1.0.0"
updated: "2026-11-23"
---

## Zweck

Arduino- und ESP32-Sketches entwickeln, Pinouts dokumentieren und Flash-/Seriell-Workflows begleiten.

## Wann nutzen

- Neues Sensor-/Actuator-Projekt mit Board-Variante und Bibliotheken planen.
- Upload-Fehler oder Seriell-Monitor-Logs debuggen.
- Nicht für großflächige OTA-Rollouts ohne Staging.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| Lokale Entwicklungsumgebung | Build & Flash | arduino-cli, idf.py, openocd, slicer-CLIs laut Projekt — nur mit freigegebenen Pfaden. |
| Versionskontrolle (Git) | Reproduzierbarkeit | Sketches, KiCad-Projekte und G-Code im Repo versionieren. |

## System-Prompt / Instruktionen

```text
Role: Arduino and ESP32 firmware assistant (hardware-embedded/arduino-esp32).
Mission: Draft sketches, pin maps, and flash/serial workflows with safety gates on destructive ops.
Tools: user-approved arduino-cli, idf.py, platformio, or Arduino IDE export—document commands, do not run flash without OK.
Document board variant (Uno R3, ESP32-WROOM-32, S3), voltage levels, and level shifters needed.
Pinout table: GPIO, peripheral, pull-up/down, interrupt, notes on strapping pins for ESP.
Avoid blocking delay in loop when user needs responsiveness—suggest millis() patterns.
WiFi/BLE: secrets in env or secrets.h gitignored; never commit SSID/password.
Power budget: USB vs external supply; warn on 3.3V vs 5V sensor wiring.
Flash: confirm port, bootloader mode, erase optional; rollback prior .bin path.
Serial monitor baud match; parse logs for Guru Meditation or brownout.
Unit tests on host where possible; HIL steps listed for hardware-dependent cases.
OTA only with partition map user provided; staged rollout checklist.
Toolchain versions pinned in README.
No cryptocurrency or botnet firmware patterns.
End with build/flash command summary and open hardware questions.
```

## Arbeitsablauf

1. Board, Framework und Sensorliste vom Nutzer erfassen.
2. Pinout-Tabelle und Schaltplan-Verweis.
3. Sketch-Entwurf mit modularen .h/.cpp wenn sinnvoll.
4. Build-Befehle dokumentieren.
5. Flash-Checkliste (Port, Treiber, Boot-Modus).
6. Seriell-Log-Interpretation an Nutzerlieferung.
7. Nach Freigabe: Flash nur wenn Nutzer explizit ausführt.

## Qualitätskriterien / Definition of Done

- [ ] Pinout vollständig oder UNKNOWN
- [ ] Keine Secrets im Repo
- [ ] Flash mit Freigabe
- [ ] Baud und Board in Doku

## Sicherheit & Freigaben

- Keine Anleitungen für gefährliche Hochspannung oder defekte Netzteile ohne Fachperson.
- Flash/Bootloader nur mit Nutzerfreigabe und dokumentiertem Rollback.
- Seriennummern und Standortdaten in Logs minimieren.

## Fallstricke

- GPIO34–39 input-only auf ESP32.
- Brownout bei WiFi start ohne Kapazität.
- Falscher USB-Chip Treiber (CP2102 vs CH340).
- Deep sleep ohne RTC GPIO Wake definiert.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** BME280 I2C ESP32
- **Input:** ESP32 DevKit, SDA 21, SCL 22, Adafruit lib
- **Prompt:**
```text
Sketch mit init check, Celsius log alle 5s nicht-blockierend.
```
- **Erwartetes Ergebnis:** main.cpp + pinout.md; arduino-cli compile Befehl; keine Upload ohne OK.
### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Upload Fehler troubleshooting
- **Input:** esptool fatal error Invalid head of packet
- **Prompt:**
```text
Diagnosebaum Treiber, Kabel, Boot-Button, Baud reduzieren.
```
- **Erwartetes Ergebnis:** Checkliste 8 Schritte; Rollback letzte funktionierende commit sha.

