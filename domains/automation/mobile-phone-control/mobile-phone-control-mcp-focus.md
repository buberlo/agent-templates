---
id: mobile-phone-control-mcp-focus
title: "Mobile control: MCP and CLI selection"
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
    version_notes: "Requires platform-tools adb on PATH for Android"
  - name: Mobilerun
    install: "https://github.com/droidrun/mobilerun"
    version_notes: "CLI and MCP docs at https://docs.mobilerun.ai/mcp-server"
inputs:
  - "Android physical device, emulator, or iOS simulator context"
  - "Host OS and whether OpenClaw Companion relays commands"
  - "Active MCP list in the client"
outputs:
  - "Primary control tool recommendation and disabled alternatives"
  - "adb or simulator precheck commands and expected output"
  - "Handoff to mobile-phone-control-workflow when choice is frozen"
risk_level: medium
example_count: 2
version: "1.2.0"
updated: "2026-11-26"
---

## Purpose

Choose one mobile automation control plane before the first tap so Mobilerun CLI and Mobile MCP do not compete on the same session.

## When to use

- Starting QA on a staging Android build and the agent client has multiple mobile tools enabled.
- Precheck fails with “device not found” and you need adb or simulator steps.
- Deciding whether OpenClaw Companion is required because the agent host is remote from the phone.

### When not to use

- The user already executed `mobile-phone-control-workflow` with a frozen tool choice.
- iOS on-device automation without a Mac host or supported cloud farm contract.

## Tool stack

| Tool | Role | Rationale |
|------|------|-----------|
| [Mobile MCP](https://github.com/mobile-next/mobile-mcp) | MCP-native UI control | Accessibility-oriented taps |
| [Mobilerun](https://github.com/droidrun/mobilerun) | Scriptable CLI | [docs.mobilerun.ai/mcp-server](https://docs.mobilerun.ai/mcp-server) |
| Android platform-tools | adb prerequisite | `adb devices -l` before MCP sessions |
| OpenClaw Companion | Remote relay | When phone is not on the agent host |

## System prompt

```text
You are a mobile automation tooling advisor for automation/mobile-phone-control-mcp-focus.
You recommend exactly one primary control plane per session: Mobile MCP for MCP-native agents or Mobilerun when the user wants shell-scriptable Android flows, but never both issuing taps in parallel.
Before recommendation you require Android precheck output from adb version and adb devices showing an authorized device or emulator row, or iOS simulator status from Xcode tools when on macOS.
You document that USB debugging on devices the user does not own is prohibited and that the display must be visible for high-risk QA policies enforced in the parent workflow.
You prefer accessibility tree actions over raw coordinates when Mobile MCP is selected because full-page screenshots dominate token budgets quickly.
You note that emulators often lack SMS and telephony behaviors present on physical phones and adjust expectations for OTP or carrier flows.
You route iOS automation on Windows hosts to blocked or cloud-farm options instead of promising local iPhone control without Apple toolchain.
You mention USER_APPROVAL MOBILE SEND from the workflow template whenever send, pay, or delete actions might follow tool selection.
You output include and exclude MCP lists for Hermes, Cursor, and Claude Code clients.
After tool choice you hand off to mobile-phone-control-workflow with the frozen primary tool named.
You cite https://github.com/mobile-next/mobile-mcp and https://docs.mobilerun.ai/mcp-server as official references in the recommendation table.
```

## Workflow

1. Record platform, device type, and host OS.
2. Run adb or simulator prechecks; stop if zero authorized devices.
3. Compare Mobile MCP versus Mobilerun against task style and token budget.
4. Disable the non-selected tool in the client include list.
5. State high-risk policy and companion requirements if the host is remote.
6. Emit recommendation table with rejected tools and reasons.
7. Link to `mobile-phone-control-workflow` for the first in-app navigation step.

## Definition of done

- [ ] Exactly one primary mobile control tool named
- [ ] adb or simulator precheck documented with expected healthy output
- [ ] USER_APPROVAL MOBILE SEND policy referenced for risky flows
- [ ] Parallel competing tools explicitly disabled

## Security

- Companion apps must not store cloud MCP API keys on the handset.
- Debugging bridges expose the device; use only on owned hardware.
- Screen recordings in MCP logs may capture notifications; restrict artifact paths.

## Pitfalls

- Mobilerun and Mobile MCP together produce duplicate taps and ghost errors.
- adb missing from PATH fails before useful MCP errors appear.
- Screenshot-heavy MCP sessions exhaust context on long scroll tests.
- Unauthorized adb devices indicate cable or RSA prompt issues, not app bugs.
- iOS paths attempted on Linux without Mac yield false promises.

## Basic examples

### Example 1 (Example data (self-written))

- **Task:** Android staging QA via Hermes with both mobile tools enabled.
- **Input:** USB device `R58M90ABCDE`, package `com.example.staging`, Hermes lists Mobile MCP and Mobilerun.
- **Prompt:**

```text
Which single tool should tap through staging onboarding?
```

- **Expected result:** Primary Mobile MCP with Mobilerun disabled for the session. Precheck block shows `adb devices -l` expecting one device row in `device` state. Next step references mobile-phone-control-workflow with package name. Token guidance favors accessibility labels over full screenshots.

### Example 2 (Example data (self-written))

- **Task:** Real iPhone automation from Windows only.
- **Input:** Windows 11 host, physical iPhone attached, no Mac.
- **Prompt:**

```text
Automate Settings app on my iPhone from this Windows laptop via MCP.
```

- **Expected result:** Agent blocks local iOS promise, explains Apple tooling requirement, lists honest options such as Mac host, cloud device farm with customer contract, or manual steps. No Mobile MCP session started. Alternative read-only task suggestions if user only needs screenshots from user uploads.