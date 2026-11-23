---
id: iot-workflow
title: "IoT"
domain: automatisierung
category: iot
tags:
  - iot
  - automatisierung
  - mqtt
target_agents:
  - hermes
  - grokbot
  - generic-mcp-agents
  - generic
required_tools:
  - name: MQTT broker
    install: "mosquitto / homeassistant MQTT"
    version_notes: "TLS empfohlen"
inputs:
  - "Broker, Topics, read vs write"
outputs:
  - "Topic-Doku und Test-Payload"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Zweck

IoT über **MQTT/HA** anbinden: erst lesen, Aktoren nur mit `FREIGABE IOT ACTUATE`.

## Wann nutzen

- Sensor auslesen, HA-Automation Draft.

## Tool-Stack

| Tool | Rolle | Begründung |
|------|-------|------------|
| mosquitto_sub/pub | CLI | Test |
| Home Assistant | Hub | Abstraktion |

## System-Prompt / Instruktionen

```text
Role: IoT integrator (automatisierung/iot).
mqtt read: mosquitto_sub -h broker -t 'home/sensor/+/state' -C 5
write only after FREIGABE IOT ACTUATE.
TLS mqtts 8883; no open 1883 on internet.
HA automation yaml active false until approval.
```

## Arbeitsablauf

1. Broker und Auth erfassen.
2. mosquitto_sub Probe.
3. Schema dokumentieren.
4. Schreibtest mit Freigabe.
5. HA Draft inactive.
6. Monitoring definieren.
7. Segmentierung notieren.

## Qualitätskriterien / Definition of Done

- [ ] Topic-Map
- [ ] Lesetest ok
- [ ] Kein offener Broker

## Sicherheit & Freigaben

- TLS und Auth.

## Fallstricke

- Retained ON auf Relais.
- Wildcard MQTT-Flut.

## Grundbeispiele

### Beispiel 1 (Beispieldaten)

- **Aufgabe:** Temperatur lesen
- **Input:** `home/bedroom/temp`
- **Prompt:**

```text
mosquitto_sub 5 msgs schema.
```

- **Erwartetes Ergebnis:**

```text
payloads logged
```

### Beispiel 2 (Beispieldaten)

- **Aufgabe:** Heizung ON
- **Input:** ohne Freigabe
- **Prompt:**

```text
Publish ON heating/cmd.
```

- **Erwartetes Ergebnis:**

```text
FREIGABE IOT ACTUATE required
```