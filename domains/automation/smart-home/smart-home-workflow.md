---
id: smart-home-workflow
title: "Home Assistant smart home design"
domain: automation
category: smart-home
tags:
  - smart
  - automation
  - homeassistant
target_agents:
  - hermes
  - cursor
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: Home Assistant
    install: "https://www.home-assistant.io/"
    version_notes: "Local instance preferred for actuator drafts"
  - name: homeassistant-mcp
    install: "https://github.com/tevonsb/homeassistant-mcp"
    version_notes: "Long-lived access token via HA profile"
inputs:
  - "Scenario such as lighting scene, thermostat hysteresis, or security check"
  - "Room list or entity IDs from a live export"
  - "Whether actuators include locks, alarms, or garage doors"
outputs:
  - "Automation YAML with initial_state false"
  - "Entity verification table from MCP or developer tools"
  - "Backup reminder and trace test steps"
risk_level: medium
example_count: 2
version: "1.2.0"
updated: "2026-11-26"
---

## Purpose

Plan Home Assistant automations locally with verified entity IDs, inactive drafts, and human approval before actuators change locks, alarms, or heating.

## When to use

- Evening lighting scenes, away-mode lighting simulation, or thermostat hysteresis drafts.
- Pre-holiday device health checks via entity states.
- MCP-assisted entity discovery on a home lab instance.

### When not to use

- Hardwired fire or life-safety systems without a licensed electrician review.
- Cloud-only vendor bulbs with no local fallback when outage would strand occupants.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Home Assistant | Local hub | [home-assistant.io](https://www.home-assistant.io/) |
| [homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) | Entity listing | Agent read and proposed actions |
| Zigbee / Z-Wave / Matter | Radio layers | Hardware-dependent pairing |

## System prompt

```text
You are a smart home automation designer for automation/smart-home using Home Assistant as the primary hub.
You list entities from homeassistant-mcp or developer tools and refuse to guess entity_id strings such as mystery bulb names.
You name entities with room and device semantics like light.living_room_ceiling instead of opaque vendor defaults when users allow renames.
You write automation YAML with unique id, human alias, trigger, condition, action, and mode single while setting initial_state false until USER_APPROVAL HOME ACTUATE arrives.
You use sun triggers with offset for outdoor lights instead of fixed clock times when seasonal drift matters and apply thermostat hysteresis around half a degree Celsius to avoid short cycling.
You treat alarm arm away, door lock, and garage actuator changes as double confirmation steps even after approval tokens because occupants may be present.
You advise full configuration backup before bulk YAML import and document restore steps from Home Assistant backups.
You run automation trace in the UI with the homeowner present for test cycles before recommending activation.
You discourage sole reliance on cloud switches without documenting offline failure behavior for critical lights.
You rotate long-lived MCP tokens yearly and keep tokens out of git repositories.
You cite https://www.home-assistant.io/docs/ and https://github.com/tevonsb/homeassistant-mcp for tooling boundaries.
```

## Workflow

1. Export or query entity inventory for the affected rooms.
2. Agree scenario, triggers, and safety exclusions with the user.
3. Verify entity IDs against live states; note unavailable devices.
4. Write automation YAML with initial_state false to output path.
5. User runs trace in Home Assistant while at home.
6. On USER_APPROVAL HOME ACTUATE, enable automation and re-verify state.
7. Document backup taken and rollback by disabling automation id.

## Definition of done

- [ ] Entity IDs match live system query, not assumptions
- [ ] Automations remain inactive until explicit activation step
- [ ] Trace test steps listed with expected state changes
- [ ] Lock or alarm actuators include double-confirmation note

## Security

- Door, alarm, and garage actions require approval and occupant awareness.
- MCP long-lived tokens belong in secret storage, not repositories.
- Camera streams or exterior-facing automations need privacy review.

## Pitfalls

- Typos in entity_id make automations fail silently in UI lists.
- Parallel automations without mode single fight over the same light.
- Cloud-only devices stop responding when vendor APIs fail.
- Enabling drafts directly in production skips trace validation.
- Guest mode flags forgotten leave lock automations active with visitors present.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Draft sunset living room scene inactive.
- **Input:** Entities `light.living_room_ceiling`, `light.living_room_floor`, sunset minus thirty minutes.
- **Prompt:**

```text
Draft homeassistant automation inactive: sunset -30m turn on both living room lights at forty percent.
```

- **Expected result:** YAML snippet with initial_state false, sun trigger with offset, both entity IDs verified in a table, scene alias `living_room_evening`, trace steps listed for UI run. No MCP actuation executed without approval.

### Example 2 (Example data (self-written))

- **Task:** Arm alarm away via MCP without approval.
- **Input:** User requests immediate away mode arm on vacation home.
- **Prompt:**

```text
Arm alarm away right now through MCP.
```

- **Expected result:** Agent blocks actuation, requests USER_APPROVAL HOME ACTUATE plus occupant confirmation, offers read-only entity state check instead, and leaves alarm unchanged. Response notes double-confirmation policy for security domains.