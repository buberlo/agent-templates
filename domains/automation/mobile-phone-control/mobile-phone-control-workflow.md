---
id: mobile-phone-control-workflow
title: "Mobile and Phone Control"
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
    version_notes: "Android adb / iOS simulator; Device USB or reachable"
  - name: Mobilerun (ehem. DroidRun)
    install: "https://github.com/droidrun/mobilerun"
    version_notes: "Alternative CLI-Steuerung Android"
inputs:
  - "Platform (Android/iOS), device ID (`adb devices`)"
  - "Target app package or visible app name"
  - "Allowed actions (tap, type, scroll) and approval for sending/paying"
outputs:
  - "Step protocol with screenshots"
  - "Erfolg/Misserfolg je UI-Zustand"
risk_level: high
example_count: 2
version: "1.1.0"
updated: "2026-11-23"
---
## Purpose

Control mobile devices **visible and controlled**: test app flows, automate repetitive taps — with mobile mcp or mobile run, without secret background actions.

## When to use

QA-Smoke on Android-Build (Staging-APK).
Accessibility checks in real app UI.


######## When not to use


- Banking/crypto without explicit user sharing per tap.
- Device without physical visibility of the user (policy).

## Tool stack

| Tool | Role | Rationale |
|-----------------------------------------------------------------------------------------------------------------
| Mobile MCP | Agent UI Control | Standard for MCP Agents |
| adb | Prerequisite Android | `adb devices`, `adb shell` |
| Mobilerun | CLI alternative | scriptable actions |

## System prompt

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

Forbidden without USER_APPROVAL MOBILE SEND: send SMS, post social, confirm payment, delete data.
Airplane mode, factory reset, uninstall app—always forbidden.
Log: timestamp, action, element description, screenshot path.
End: return device to home screen.
```

## Workflow

1. User confirmed device connected and screen visible.
2. Check `adb devices` (Android) or simulator status (iOS).
3. Target app and allowed actions in writing.
4. Mobile MCP: Launch app, first screen screenshots.
5. Flow step by step; after fill/tap screenshot and assertion.
6. Send/pay only after `FREEGABE MOBILE SEND`.
7. home screen; Protocol to users.

## Definition of done

- [ ] Device ID in the protocol
- [ ] No OTP/passwords typed from chat
- [ ] Screenshots of critical steps
- [ ] High-risk actions with release or not executed

## Security

- high risk: Remote control only with consent and visible display.
- Do not store cloud MCP keys on device.

## Pitfalls

- Enable only required tools.

- Multiple `adb devices` → false tap.
- Overlay advertising blocks target button.
iOS without Developer Trust → MCP fails.

## Basic examples

Example 1 (Example data)

- **Task:** Staging app Login screen reach
- **Input:** `com.firma.staging`, device `R58M90ABCDE`
- **Prompt:**

```text
mobile-mcp open app, screenshot login, fill test user from env, do NOT tap submit until approval.
```

- **Expected result:**

```text
screenshots/01_login.png | submit not pressed | adb device logged
```
Example 2 (Example data)

- **Task:** Confirm payment
- **Input:** without FREEDOM
- **Prompt:**

```text
Tap Pay now on checkout.
```

- **Expected result:**

```text
action blocked | request USER_APPROVAL MOBILE SEND
```

## Basic examples

### Example 1 (Example data)

- **Task:** Minimal dry run
- **Input:** Example briefing (labeled example data)
- **Prompt:**
```text
Follow the workflow with no external side effects.
```
- **Expected result:** Draft output paths listed; no production changes.

### Example 2 (Example data)

- **Task:** Review-only pass
- **Input:** Same briefing as Example 1
- **Prompt:**
```text
Produce checklist only; no sends or deployments.
```
- **Expected result:** Checklist with explicit approval gates marked.
