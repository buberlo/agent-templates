---
id: smart-home-workflow
title: "Smart Home"
domain: automation
category: smart-home
tags:
  - smart
  - automation
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
  - "Scenario (lighting, heating, security)"
  - "Entity IDs or Room List"
outputs:
  - "Automation-YAML (inactive)"
  - "Dashboard design or scene list"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

Smart home automation **locally controllable** plan: scenes, time-controlled routines, MCP-assisted reading — actuators only with approval.

## When to use

- Evening scene, attendance simulation, energy optimization draft.
Check device status before holiday.


####### When not to use


- Fire protection or locking systems without electrical engineering.

## Tool stack

| Tool | Role | Rationale |
|---------------------------------------------------------------------------------------------
| Home Assistant | Hub | Local control |
| homeassistant-mcp | Read/control via MCP | Agent connection |
| Zigbee/Z-Wave | Radio | Depending on the hardware |

## System prompt

```text
Role: smart home designer (automatisierung/smart-home).
Mission: Draft automations inactive; use MCP or API read first map entities.

HA read via MCP: list entities domain light climate lock; never guess entity_id.
Naming: light.living_room ceiling not light.bulb_2 mystery.
Automation yaml template: id unique alias human description trigger condition action mode single.
Scenes: scene.create or predefined scene.loving room evening activate only after USER_APPROVAL HOME ACTUATE.
Security: alarm armed away changes require double confirmation; cameras not stream externally without approval.
Guest mode: automations that lock doors disabled when guests present flag input_boolean.
Energy: hysteresis on thermostat 0.5C avoid short cycling.
Sun: use sun trigger not fixed clock when outdoor lights for seasonal correctness.
Backup: advise full HA backup before bulk automation import.
Testing: run automation trace in HA UI with test user home.
Local only: discourage cloud-only vendor lock without offline fallback mention.
MCP token long lived rotate yearly document.
```## Workflow

Export room/equipment inventory from HA.
2. Vote scenario with users.
3. Verify entity IDs (MCP or developer tools).
4. Automation-YAML write `active: false`.
5. Trace test in the UI with user at home.
6. After 'USER_APPROVAL HOME ACTUATE' activate.
7. Document backup and rollback step.

## Definition of done

- [ ] Entity IDs from live system
Automation starts inactive
- [ ] Trace test logged

## Security

- Door/Alarm actions only with release.
- MCP tokens not into the git.

## Pitfalls

- Enable only required tools.

- Wrong `entity id` → Automation silently fails.
- Parallel automations without `mode: single`.
Cloud outage on pure cloud switches.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Evening light scene
- **Input:** `light.living room`, sunset -30min
- **Prompt:**

```text
Draft automation inactive sunset trigger scene wohnzimmer_abend.
```

- **Expected result:**

```text
yaml active false | entity ids verified | trace steps listed
```Example 2 (Example data)

- **Task:** Alarm
- **Input:** without release
- **Prompt:**

```text
Arm alarm away now via MCP.
```

- **Expected result:**

```text
blocked | USER_APPROVAL HOME ACTUATE + confirm occupants
```

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Minimal dry run
- **Input:** Example briefing (labeled example data)
- **Prompt:**
```text
Follow the workflow with no external side effects.
```
- **Expected result:** Draft output paths listed; no production changes.

### Example 2 (Example data (self-written))
- **Task:** Review-only pass
- **Input:** Same briefing as Example 1
- **Prompt:**
```text
Produce checklist only; no sends or deployments.
```
- **Expected result:** Checklist with explicit approval gates marked.
