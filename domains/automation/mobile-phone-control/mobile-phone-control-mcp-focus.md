---
id: mobile-phone-control-mcp-focus
title: "Mobile and Phone Control: MCP/Skill Focus"
domain: automation
category: mobile-phone-control
tags:
  - mobile
  - automation
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
  - name: Mobilerun (formerly DroidRun)
    install: "https://github.com/droidrun/mobilerun"
    version_notes: "Parallel CLI only when the user wants it"
inputs:
  - "Client platform and active MCP list"
  - "Android vs iOS vs Companion-App"
outputs:
  - "Recommended MCP and companion pairing"
  - "Precheck commands (adb, simulator)"
risk_level: medium
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

**mobile-mcp vs. Mobilerun vs. Companion** route: minimal setup, adb requirements, policy for high-risk actions before the first tap.

## When to use

- Clarify before a mobile automation session tool landscape.
- Error "no device found" → Prechecklist.

## Tool stack

| Tool | Role | Rationale |
|--------------------------------
| Mobile MCP | UI automation | MCP-native agents |
| Mobilerun | CLI | Scriptable Android flows |
| OpenClaw Companion | Relay | Non-agent host |

## System prompt

```text
Role: mobile MCP advisor (automatisierung/mobile-phone-control-mcp-focus).
Mission: Select one primary control plane; document adb/simulator prerequisites.

Android path: platform-tools; USB debugging; adb devices authorized.
Mobile MCP config: add server mobile-mcp; prefer accessibility tree taps.
Mobilerun: when user wants shell scripts without full MCP snapshot cost.
Do not run Mobilerun and Mobile MCP competing taps same session.
High risk: USER_APPROVAL MOBILE SEND token in parent workflow.
Precheck: adb version; adb devices -l; package grep fragment.
Handoff to mobile-phone-control-workflow after tool choice frozen.

Document emulator vs physical device policy; emulators may lack SMS/telephony.
Simulator iOS path uses Xcode tools—not interchangeable with Android adb.
```

## Workflow

1. Enquire platform and device type.
2. Precheck commands.
3. Mobile MCP vs Mobilerun.
Suggest include list.
5. Call it a high-risk policy.
6. Reference to workflow template.

## Definition of done

- [ ] Exactly one primary control tool recommended
- [ ] adb Precheck documented
- [ ] FREE MOBILE SEND mentioned

## Security

- Companion app ≠ storage for API keys.

## Pitfalls

- Two controls in parallel → Ghost-taps and double sends.
- MCP without adb on PATH → immediate error; "Which adb" before the session.
- Full-page MCP screenshots expensive in token budget — Prefer accessibility tree.
- USB debugging on third-party devices without owner sharing - prohibited.

## Basic examples

### Example 1 (Example data (self-written))
- **Task:** Tool choice Android QA
- **Input:** Hermes, USB device
- **Prompt:**

```text
Which MCP for tap-through staging app?
```

- **Expected result:**

```text
mobile-mcp primary | adb devices checklist
```

### Example 2 (Example data (self-written))
- **Task:** iOS without Mac
- **Input:** Windows host
- **Prompt:**

```text
Automate iOS app on real iPhone.
```

- **Expected result:**

```text
block or cloud farm | no false promise local iOS
```

### Example 2 (Example data (self-written))
- **Task:** Second dry run
- **Input:** Example data only
- **Prompt:**
```text
Repeat workflow; no external writes.
```
- **Expected result:** Checklist only.
