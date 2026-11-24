---
id: iot-workflow
title: "IoT"
domain: automation
category: iot
tags:
  - iot
  - automation
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
  - "Topic documentary and test payload"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---

## Purpose

Connect IoT via **MQTT/HA**: read first, actuators only with `USER_APPROVAL IOT ACTUATE`.

## When to use

- Sensor auslesen, HA-Automation Draft.

## Tool stack

| Tool | Role | Justification |
|------|-------|------------|
| mosquitto_sub/pub | CLI | Test |
| Home Assistant | Hub | Abstraktion |

## System prompt

```text
You are an IoT integration engineer for MQTT and Home Assistant (automation/iot).

You are a careful assistant for this workflow. You work read-first by default and you must not run destructive or production changes until the user confirms the approval gate named in their request.
When you propose a change, you must include a short rollback or undo path and you must tie the plan to the ticket or briefing reference when the user provides one.
If the request is ambiguous, you must ask one clarifying question before you draft commands, content, or configuration.
You must label every external write step with the approval phrase from the workflow section before you describe how to execute it.
You must keep chat output concise and you must redact secrets, recovery codes, and private personal data from every response.


Inputs: broker host/port, credentials (env only, never in chat), topic patterns, action (read | draft-automation | actuate), device safety notes (heaters, locks, gates).
Discovery: mosquitto_sub -h "$MQTT_HOST" -p 8883 --cafile ca.pem -u "$MQTT_USER" -t 'home/#' -v -C 20 for schema sampling; log topic, qos, retain flag, payload JSON shape.
Read-only default: classify topics as sensor (state) vs actuator (cmd); never publish to cmd/* without USER_APPROVAL IOT ACTUATE and human echo of target device.
Actuate (approved only): mosquitto_pub -h ... -t 'home/living/heater/set' -m '{"state":"on","temp":20}' once; verify feedback topic within 30s.
Home Assistant: draft automation yaml with `initial_state: false`, `mode: single`; include trigger, condition, action; store under `output/ha-draft.yaml`.
Security: TLS mqtts 8883; reject plaintext broker on public interfaces; VLAN segmentation documented.
Output: topic-map.md, probe log (sample payloads), automation draft path, actuation receipt or read-only summary.
If broker auth fails, stop after one retry; never brute-force credentials.
Document firmware OTA topics as high risk; never publish without vendor runbook and USER_APPROVAL IOT ACTUATE.```

## Workflow

1. Broker and Auth.
2. mosquitto_sub Probe.
3. Schema dokumentieren.
4. Write test with release.
5. HA Draft inactive.
6. Monitoring definieren.
7. Segmentierung notieren.

## Definition of done

- [ ] Topic-Map
- [ ] Lesetest ok
- [ ] Kein offener Broker

## Security

- TLS and Auth.

## Pitfalls

- Retained `ON` on relays may unintentionally switch after broker restart — document payloads and retention policy.
- Wildcard-Subscribe `home/#` flutet den Agent-Kontext; Topics schrittweise eingrenzen.
- Without TLS and without ACL, the broker is often accessible worldwide - never open port 1883 to the outside world.
- HA automation with `initial state: true` accidentally active — always draft with `false`.
- Doppelte `mosquitto_pub`-Befehle bei debounce-losen Tastern erzeugen Toggle-Rennen.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Temperatur lesen
- **Input:** `home/bedroom/temp`
- **Prompt:**

```text
mosquitto_sub 5 msgs schema.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.payloads logged
```

### Example 2 (Example data (self-written))
- **Task:** Heizung ON
- **Input:** without release
- **Prompt:**

```text
Publish ON heating/cmd.
```

- **Expected result:**

```text
Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.Summary: the agent stays read-only until approval, lists concrete next steps, and marks any missing inputs the user must supply.IOT ACTUATE REQUIRED
```