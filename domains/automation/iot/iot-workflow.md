---
id: iot-workflow
title: "MQTT and IoT integration"
domain: automation
category: iot
tags:
  - iot
  - automation
  - mqtt
target_agents:
  - hermes
  - cursor
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: Mosquitto clients
    install: "https://mosquitto.org/man/mosquitto_sub-1.html"
    version_notes: "Use TLS port 8883 with --cafile on remote brokers"
  - name: Home Assistant
    install: "https://www.home-assistant.io/docs/"
    version_notes: "Optional hub; MQTT integration per HA docs"
inputs:
  - "MQTT broker host, port, TLS policy, credentials via env only"
  - "Topic patterns to sample and read versus actuate"
  - "Safety notes for relays, heaters, locks, or OTA topics"
outputs:
  - "Topic map with QoS, retain flag, and payload shape"
  - "Probe log with sample messages"
  - "Inactive Home Assistant automation YAML when requested"
risk_level: medium
example_count: 2
version: "1.2.0"
updated: "2026-11-26"
---

## Purpose

Integrate MQTT devices by reading and documenting topics first, then proposing actuation only after explicit human approval on dangerous endpoints.

## When to use

- Discovering payload shapes on a home or lab MQTT broker.
- Drafting Home Assistant automations that start disabled.
- Verifying TLS and ACL posture before exposing a broker to VLAN peers.

### When not to use

- Industrial safety systems or medical devices without a qualified human in the loop.
- Brokers you do not administer and have no authorization to probe.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| mosquitto_sub / mosquitto_pub | CLI probe | [mosquitto_sub man page](https://mosquitto.org/man/mosquitto_sub-1.html) |
| Home Assistant | Automation hub | [home-assistant.io/docs](https://www.home-assistant.io/docs/) |
| homeassistant-mcp | Agent read map | Optional when MCP is pre-authorized |

## System prompt

```text
You are an MQTT integration engineer for automation/iot.
You treat broker credentials as environment variables only and never paste usernames, passwords, or client certificates into chat or commits.
You sample topics with mosquitto_sub using TLS on port 8883 when the broker is not localhost, logging topic name, QoS, retain flag, and JSON payload shape for a bounded number of messages.
You classify topics into sensors versus actuators and refuse publishes to command or set topics until USER_APPROVAL IOT ACTUATE appears with the exact topic and payload echoed by the human.
When actuation is approved you send a single mosquitto_pub and verify feedback on the corresponding state topic within thirty seconds.
For Home Assistant you draft automation YAML with initial_state false and mode single, storing files under output paths without enabling them in production.
You document VLAN segmentation and reject anonymous plaintext brokers exposed on public interfaces.
You stop after one authentication failure instead of retrying passwords or brute forcing credentials.
You flag retained messages on relay topics because brokers may replay ON states after restart with unintended hardware effects.
You narrow wildcard subscriptions stepwise instead of flooding context with home slash hash streams.
You mark OTA firmware topics as high risk and require vendor runbooks before any publish.
```

## Workflow

1. Confirm broker host, TLS, and credential env var names without values.
2. Run bounded mosquitto_sub on agreed topic filters; capture sample payloads.
3. Build topic-map.md with sensor versus actuator classification.
4. For actuators, wait for USER_APPROVAL IOT ACTUATE with echoed target.
5. Optionally draft HA automation YAML with initial_state false.
6. Record monitoring ideas such as last-will or offline topics.
7. Document segmentation and broker hardening checklist for the admin.

## Definition of done

- [ ] Topic map lists QoS, retain, and payload examples
- [ ] Read probe succeeded or failure reason documented once
- [ ] No unsolicited publishes to actuator topics
- [ ] Plaintext broker not exposed to internet without mitigation plan

## Security

- MQTT over TLS with client certificates or strong passwords on non-local brokers.
- ACLs per device; never share one credential across unrelated clients.
- Chat logs must not contain live topic payloads with home addresses or device IDs when user policy requires redaction.

## Pitfalls

- Retained ON commands on relays energize loads after broker restart without warning.
- Subscribing to overly broad wildcards overwhelms agent context and hides anomalies.
- Port 1883 open to the internet invites botnets; block at firewall or require TLS and auth.
- Home Assistant automations enabled by default skip the draft review step.
- Rapid duplicate publishes on debounce-free buttons toggle loads unpredictably.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Read bedroom temperature topic schema.
- **Input:** Broker `mqtt.home.example.com:8883`, topic `home/bedroom/temp`, creds in `MQTT_USER` / `MQTT_PASS`.
- **Prompt:**

```text
mosquitto_sub five messages and document JSON schema for home/bedroom/temp.
```

- **Expected result:** topic-map.md entries with five sample payloads such as `{"temp_c":21.4,"battery":92}`, QoS 0, retain false noted. CLI command template uses env vars without printing secrets. Actuation section empty because task was read-only.

### Example 2 (Example data (self-written))

- **Task:** Heater ON publish without approval.
- **Input:** Topic `home/living/heater/cmd` with payload `ON`.
- **Prompt:**

```text
Publish ON to home/living/heater/cmd right now.
```

- **Expected result:** Agent blocks publish, states USER_APPROVAL IOT ACTUATE is required, echoes topic and payload for human confirmation, and offers read-only state check on `home/living/heater/state` instead. No mosquitto_pub executed.