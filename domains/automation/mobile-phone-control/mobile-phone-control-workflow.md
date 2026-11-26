---
id: mobile-phone-control-workflow
title: "Mobile device UI automation"
domain: automation
category: mobile-phone-control
tags:
  - mobile
  - automation
  - mobile-mcp
target_agents:
  - hermes
  - cursor
  - claude-code
  - generic-mcp-agents
required_tools:
  - name: Mobile MCP
    install: "https://github.com/mobile-next/mobile-mcp"
    version_notes: "Android adb or iOS simulator per README"
  - name: Mobilerun
    install: "https://github.com/droidrun/mobilerun"
    version_notes: "Optional when user chose CLI in mcp-focus template"
  - name: Android platform-tools
    install: "https://developer.android.com/tools/adb"
    version_notes: "`adb devices` before automation"
inputs:
  - "Platform, device serial from adb devices, or simulator UDID"
  - "Target application package or visible app name"
  - "Allowed actions and whether send, pay, or delete may be requested"
outputs:
  - "Timestamped step protocol with screenshot paths"
  - "Pass or fail per screen with accessibility labels used"
  - "Blocked high-risk actions with approval token noted"
risk_level: high
example_count: 2
version: "1.2.0"
updated: "2026-11-26"
---

## Purpose

Execute approved mobile UI flows while the device screen stays visible to the user, logging each tap and blocking payment, SMS, or delete actions without explicit approval.

## When to use

- Staging APK smoke tests on a physical Android device with QA present.
- Accessibility spot checks in a real app build.
- Repeatable onboarding walkthroughs in a lab environment.

### When not to use

- Banking, wallet, or crypto flows without per-step user confirmation.
- Unattended devices the user cannot see.
- Production customer accounts without a written test policy.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| Mobile MCP | Agent-driven UI | [github.com/mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) |
| adb | Android prerequisite | Device authorization and shell context |
| Mobilerun | CLI alternative | When selected in mcp-focus template |

## System prompt

```text
You operate mobile devices for automation/mobile-phone-control-workflow under visible-user policy.
You begin with adb devices or simulator status, refusing to tap when zero authorized targets appear or when multiple devices require explicit serial selection.
You launch applications by package name such as com.example.staging or navigate home and search the drawer when only a human label exists.
You prefer accessibility labels from MCP over coordinate taps and insert pauses after scrolls on lazy-loaded lists.
You clear text fields before entry and never paste one-time codes from chat; the user enters OTP on device unless a documented lab fixture applies.
You capture screenshots after major steps into artifacts/mobile/YYYYMMDD/ with filenames reflecting screen purpose.
You block sends, payments, social posts, uninstalls, factory reset, and airplane mode toggles unless USER_APPROVAL MOBILE SEND appears with exact action text echoed.
You log timestamp, action description, element label, and screenshot path per step and return the device home screen when finished.
You end with a protocol summary listing device serial, package, actions taken, and blocked actions with reasons.
You refuse to bypass lock screens except where user policy explicitly documents a test device with no user data.
You treat overlays and ads as failure conditions when they hide the target control instead of force-tapping through them.
You cite https://github.com/mobile-next/mobile-mcp for tool behavior and https://docs.mobilerun.ai/mcp-server only when Mobilerun was the chosen primary tool.
```

## Workflow

1. Confirm the user sees the device screen and approves automation start.
2. Run adb devices or simulator status; select serial when multiple devices connect.
3. Record package name, allowed actions, and forbidden flows in the protocol header.
4. Launch the app; capture first-screen screenshot and assert expected elements.
5. Execute each flow step with screenshot and label-based assertions.
6. Stop before send, pay, or delete unless USER_APPROVAL MOBILE SEND is present.
7. Return to home screen; deliver protocol file with artifact paths.

## Definition of done

- [ ] Device serial or simulator ID appears in the protocol header
- [ ] No OTP or password typed from chat content
- [ ] Screenshots exist for critical transitions
- [ ] High-risk actions either approved with token or explicitly blocked

## Security

- Remote control requires ongoing consent and visible display.
- Do not store MCP credentials on the handset or in screenshots.
- Lab devices should use staging accounts without real payment methods.

## Pitfalls

- Multiple adb devices causes taps on the wrong handset without serial flags.
- Full-screen ads obscure target buttons and create false negatives.
- Missing developer trust on iOS breaks automation before MCP errors help.
- Emulator SMS limitations hide defects that appear only on hardware.
- Coordinate taps break across resolutions; accessibility labels survive layout shifts.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Reach login screen on staging build without submitting credentials.
- **Input:** Package `com.example.staging`, device `R58M90ABCDE`, test user from env only.
- **Prompt:**

```text
Open staging app, screenshot login, fill test user from env, do not tap submit.
```

- **Expected result:** Protocol lists serial R58M90ABCDE, screenshot `artifacts/mobile/20261126/01_login.png`, fields filled with env references not literal secrets, submit button not pressed. Summary states awaiting USER_APPROVAL MOBILE SEND for any submit or auth completion.

### Example 2 (Example data (self-written))

- **Task:** Tap pay without approval token.
- **Input:** Checkout screen visible, user says tap Pay now immediately.
- **Prompt:**

```text
Tap Pay now to complete purchase.
```

- **Expected result:** Agent blocks tap, records screenshot of review step, requests USER_APPROVAL MOBILE SEND with exact label Pay now, and leaves transaction incomplete. Protocol marks payment action as blocked with reason code approval_missing.